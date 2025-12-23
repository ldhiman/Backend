from fastapi import Header, HTTPException, Depends
from firebase_admin import auth as firebase_auth
from app.firebase import db
from firebase_admin import firestore


async def verify_firebase_token(authorization: str = Header(None)):
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header")

    token = authorization.split(" ")[1]

    try:
        decoded = firebase_auth.verify_id_token(token)
        # await ensure_user_exists(decoded)
        return decoded  # contains uid, email, name
    except Exception as e:
        print(e)
        raise HTTPException(status_code=401, detail="Invalid or expired token")

def credit_required(cost: int = 1):
    async def _credit_guard(user = Depends(verify_firebase_token)):
        uid = user["uid"]
        user_ref = db.collection("users").document(uid)

        @firestore.transactional
        def deduct_credit(txn):
            snap = user_ref.get(transaction=txn)
            if not snap.exists:
                raise HTTPException(status_code=404, detail="User not found")

            credits = snap.to_dict().get("credits", 0)

            if credits < cost:
                raise HTTPException(
                    status_code=402,
                    detail="Insufficient credits. Please recharge."
                )

            txn.update(user_ref, {
                "credits": credits - cost,
                "updatedAt": firestore.SERVER_TIMESTAMP
            })

        txn = db.transaction()
        deduct_credit(txn)

        return user  # pass user forward

    return _credit_guard


def subscription_required():
    async def _guard(user=Depends(verify_firebase_token)):
        uid = user["uid"]
        snap = db.collection("users").document(uid).get()

        if not snap.exists:
            raise HTTPException(status_code=404, detail="User not found")

        sub = snap.to_dict().get("subscription")

        if not sub or not sub.get("active"):
            raise HTTPException(
                status_code=403,
                detail="Cloud sync requires active subscription"
            )

        return user

    return _guard

import firebase_admin
from firebase_admin import credentials, firestore
from app.core.config import settings
import json



cred = credentials.Certificate(json.loads(settings.SERVICE_ACCOUNT))
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

db = firestore.client()
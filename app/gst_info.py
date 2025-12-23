import requests

def get_gst_info_1(gstin: str):
    url = f"https://blog-backend.mastersindia.co/api/v1/custom/search/gstin/?keyword={gstin}&unique_id=1"

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cache-control': 'no-cache',
    'dnt': '1',
    'origin': 'https://www.mastersindia.co',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://www.mastersindia.co/gst-number-search-and-gstin-verification/',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

def get_gst_info_2(gstin: str):

    url = f"https://tools.signalx.ai/apps/gst-verification/gstin-overview/{gstin}"

    headers = {
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    'cache-control': 'no-cache',
    'dnt': '1',
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': 'https://tools.signalx.ai/gstin-verification/07AAACU4747P1ZR',
    'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
    'Cookie': '_ga=GA1.1.1172065132.1766063675; _clck=qtf00r%5E2%5Eg1y%5E0%5E2178; _clsk=3tedx7%5E1766063679480%5E1%5E1%5Ej.clarity.ms%2Fcollect; messagesUtk=ea9165107b1c478aa6f21dd3edc9001d; _gcl_au=1.1.1101140264.1766063680; __hstc=219074118.b4199f4f72d7420782743b75d6e6d2c6.1766063680243.1766063680243.1766063680243.1; hubspotutk=b4199f4f72d7420782743b75d6e6d2c6; __hssrc=1; __hssc=219074118.1.1766063680243; _ga_RN3LXLE8J3=GS2.1.s1766063675$o1$g0$t1766063686$j49$l0$h0; _ga_YZEDDY0L1W=GS2.1.s1766063675$o1$g0$t1766063686$j49$l0$h0'
    }

    response = requests.request("GET", url, headers=headers)

    return response.json()

'''

GST 1 info:
{
    "success": true,
    "data": {
        "stjCd": "DL106",
        "dty": "Regular",
        "lgnm": "ROSMERTA SAFETY SYSTEMS LIMITED",
        "stj": "Ward 106",
        "adadr": [
            {
                "addr": {
                    "bnm": "Pul Prahlad Pur,",
                    "st": "M. B. Road, Badarpur",
                    "loc": "New Delhi",
                    "bno": "RZA-1,",
                    "dst": "South East Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110044",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "",
                    "lg": ""
                },
                "ntr": "Factory / Manufacturing, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "C/O Sawhney Automobile",
                    "st": "Sector-3, Dwarka",
                    "loc": "New Delhi",
                    "bno": "K-24, Rajapuri",
                    "dst": "New Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110059",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "",
                    "lg": ""
                },
                "ntr": "Office / Sale Office, Warehouse / Depot"
            },
            {
                "addr": {
                    "bnm": "C/O PURI CONTRACTOR",
                    "st": "TILAK GALI, PAHARGANJ",
                    "loc": "NEW DELHI",
                    "bno": "2395",
                    "dst": "New Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110055",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "FLAT NO. 10",
                    "lg": ""
                },
                "ntr": "Office / Sale Office, Warehouse / Depot"
            },
            {
                "addr": {
                    "bnm": "C/O SHIV GANGA AUTOMOBILES",
                    "st": "MAIN ROHTAK ROAD NEAR PEERA GARHI CHOWK",
                    "loc": "NEW DELHI",
                    "bno": "A 1/2, PASCHIM VIHAR,",
                    "dst": "New Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110063",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "",
                    "lg": ""
                },
                "ntr": "Office / Sale Office, Warehouse / Depot"
            },
            {
                "addr": {
                    "bnm": "C/O PASHUPATI MOTORS",
                    "st": "SRI AUROBINDO MARG",
                    "loc": "NEW DELHI",
                    "bno": "84, ADCHINI",
                    "dst": "New Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110055",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "",
                    "lg": ""
                },
                "ntr": "Office / Sale Office, Warehouse / Depot"
            },
            {
                "addr": {
                    "bnm": "C/O OSWAL AUTO",
                    "st": "G.T.KARNAL ROAD, INDUSTRIAL AREA AZADPUR",
                    "loc": "NEW DELHI",
                    "bno": "A-20",
                    "dst": "New Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110033",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "",
                    "lg": ""
                },
                "ntr": "Office / Sale Office, Warehouse / Depot"
            },
            {
                "addr": {
                    "bnm": "C/O ESS AAY AGENCIES",
                    "st": "FAIZ ROAD, KAROL BAGH",
                    "loc": "NEW DELHI",
                    "bno": "T-2336",
                    "dst": "New Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110005",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "",
                    "lg": ""
                },
                "ntr": "Office / Sale Office, Warehouse / Depot"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Main Kanjhawala Road, Near Mohalla Clinic",
                    "loc": "VPO Ghevra",
                    "bno": "Plot No 4, Khasra No. 34/25",
                    "dst": "New Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110081",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "",
                    "lg": ""
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Main Nangloi Road",
                    "loc": "Najafgarh",
                    "bno": "Plot No 16, Khasra No. 152/22 Sultan Garden",
                    "dst": "New Delhi",
                    "lt": "",
                    "locality": "",
                    "pncd": "110043",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "NA",
                    "flno": "",
                    "lg": ""
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Opp. Gurudwara",
                    "loc": "New Delhi",
                    "bno": "2214, T/F, H Singh Road Naiwala, Karol Bagh",
                    "dst": "Central Delhi",
                    "lt": "28.6544",
                    "locality": "",
                    "pncd": "110005",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "pincode",
                    "flno": "",
                    "lg": "77.187341"
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Situated at Community Centre I",
                    "loc": "New Delhi",
                    "bno": "Shop No. S-37, Phase-I",
                    "dst": "New Delhi",
                    "lt": "28.631037",
                    "locality": "Mayapuri",
                    "pncd": "110064",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "locality",
                    "flno": "",
                    "lg": "77.1207420000001"
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Kalkaji",
                    "loc": "New Delhi",
                    "bno": "N-10",
                    "dst": "South East Delhi",
                    "lt": "28.543107",
                    "locality": "",
                    "pncd": "110019",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "pincode",
                    "flno": "Upper Ground Floor",
                    "lg": "77.257722"
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Phase-1",
                    "loc": "New Delhi",
                    "bno": "B-23",
                    "dst": "South East Delhi",
                    "lt": "28.5237030000001",
                    "locality": "Okhla Industrial Area",
                    "pncd": "110020",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "locality",
                    "flno": "",
                    "lg": "77.280241"
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Delhi",
                    "loc": "New Delhi",
                    "bno": "6B, Hasanpur",
                    "dst": "East Delhi",
                    "lt": "28.6293370000001",
                    "locality": "Indraprastha Extension",
                    "pncd": "110092",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "locality",
                    "flno": "",
                    "lg": "77.3026310000001"
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Delhi",
                    "loc": "New Delhi",
                    "bno": "J-128 3.5 Pusta",
                    "dst": "North East Delhi",
                    "lt": "28.689379",
                    "locality": "Kartar Nagar",
                    "pncd": "110053",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "locality",
                    "flno": "",
                    "lg": "77.2585110000001"
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Loni Road",
                    "loc": "New Delhi",
                    "bno": "B-28",
                    "dst": "Shahdara",
                    "lt": "28.6920235000001",
                    "locality": "Jyoti Nagar East",
                    "pncd": "110093",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "Neighbourhood",
                    "flno": "",
                    "lg": "77.2919220000001"
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "World Trade Tower",
                    "st": "Barakhamba Lane",
                    "loc": "New Delhi",
                    "bno": "Flot No. 402",
                    "dst": "New Delhi",
                    "lt": "28.6303360000001",
                    "locality": "",
                    "pncd": "110001",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "Building",
                    "flno": "4th Floor",
                    "lg": "77.2267670000001"
                },
                "ntr": "Factory / Manufacturing, Retail Business, Office / Sale Office, Warehouse / Depot, Recipient of Goods or Services"
            },
            {
                "addr": {
                    "bnm": "",
                    "st": "Ram Mandir Road",
                    "loc": "New Delhi",
                    "bno": "Khasra No 10/16/1, Behind D-4, Vasant Kunj",
                    "dst": "New Delhi",
                    "lt": "28.51498",
                    "locality": "Farm No 3, Admeasuring One Bigha 12 Biswa out of",
                    "pncd": "110070",
                    "landMark": "",
                    "stcd": "Delhi",
                    "geocodelvl": "locality",
                    "flno": "",
                    "lg": "77.1532450000001"
                },
                "ntr": "Office / Sale Office, Wholesale Business, Factory / Manufacturing, Warehouse / Depot, Retail Business"
            }
        ],
        "cxdt": "",
        "gstin": "07AAACU4747P1ZR",
        "nba": [
            "Wholesale Business",
            "Warehouse / Depot",
            "Office / Sale Office",
            "Factory / Manufacturing",
            "Recipient of Goods or Services",
            "Retail Business"
        ],
        "lstupdt": "24/05/2024",
        "rgdt": "01/07/2017",
        "ctb": "Public Limited Company",
        "pradr": {
            "addr": {
                "bnm": "",
                "st": "Rewari Line",
                "loc": "New Delhi",
                "bno": "No A-3",
                "dst": "New Delhi",
                "lt": "28.629439",
                "locality": "Mayapuri Industrial Area Phase 1",
                "pncd": "110064",
                "landMark": "",
                "stcd": "Delhi",
                "geocodelvl": "locality",
                "flno": "Ground Floor",
                "lg": "77.1265240000001"
            },
            "ntr": "Wholesale Business, Warehouse / Depot, Office / Sale Office"
        },
        "tradeNam": "ROSMERTA SAFETY SYSTEMS LIMITED",
        "sts": "Active",
        "ctjCd": "ZL0901",
        "ctj": "RANGE - 131",
        "einvoiceStatus": "Yes"
    }
}


GST 2 Info:
{
    "gstin": "07AAACU4747P1ZR",
    "legal_business_name": "ROSMERTA SAFETY SYSTEMS LIMITED",
    "trade_name": "ROSMERTA SAFETY SYSTEMS LIMITED",
    "constitution_of_business": "Public Limited Company",
    "gstin_uin_status": "Active",
    "taxpayer_type": "Regular",
    "effective_date_of_reg": "2017-07-01T00:00:00",
    "state_jurisdiction_code": "",
    "state_jurisdiction_ward": "State - Delhi,Zone - Zone 4,Ward - Ward 106 (Jurisdictional Office)",
    "central_jurisdiction_code": "",
    "central_jurisdiction_ward": "State - CBIC,Zone - DELHI,Commissionerate - DELHI WEST,Division - JANAK PURI,Range - RANGE - 131",
    "principal_place_of_business": "",
    "goods_and_services_list": [
        {
            "goods_services_desc": "INSECTICIDES, RODENTICIDES, FUNGICIDES, HERBICIDES, ANTI-SPROUTING PRODUCTS AND PLANT-GROWTH REGULATORS, DISINFECTANTS AND SIMILAR PRODUCTS, PUT UP IN FORMS OR PACKINGS FOR RETAIL SALE OR AS PREPARATIONS OR ARTICLES (FOR EXAMPLE, SULPHURTREATED BANDS, WICKS AND CANDLES, AND FLY-PAPERS)",
            "hsn_code": "3808"
        },
        {
            "goods_services_desc": "GARMENTS, MADE UP OF FABRICS OF HEADING 5602, 5603, 5903, 5906 OR 5907",
            "hsn_code": "6210"
        },
        {
            "goods_services_desc": "OTHER MADE UP ARTICLES, INCLUDING DRESS PATTERNS",
            "hsn_code": "6307"
        },
        {
            "goods_services_desc": "SIGN-PLATES, NAME-PLATES, ADDRESS-PLATES AND SIMILAR PLATES, NUMBERS, LETTERS AND OTHER SYMBOLS, OF BASE METAL, EXCLUDING THOSE OF HEADING 9405",
            "hsn_code": "8310"
        },
        {
            "goods_services_desc": "OTHER",
            "hsn_code": "76169990"
        }
    ],
    "filings": [
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2025-2026",
            "tax_period": "November",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-12-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2025-2026",
            "tax_period": "October",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-11-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2025-2026",
            "tax_period": "September",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-10-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2025-2026",
            "tax_period": "August",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-09-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2025-2026",
            "tax_period": "July",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-08-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2025-2026",
            "tax_period": "June",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-07-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2025-2026",
            "tax_period": "May",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-06-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2025-2026",
            "tax_period": "April",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-05-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2024-2025",
            "tax_period": "March",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-04-11T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR-1/IFF",
            "financial_year": "2024-2025",
            "tax_period": "February",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-03-10T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2025-2026",
            "tax_period": "November",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-12-18T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2025-2026",
            "tax_period": "October",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-11-20T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2025-2026",
            "tax_period": "September",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-10-24T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2025-2026",
            "tax_period": "August",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-09-20T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2025-2026",
            "tax_period": "July",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-08-20T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2025-2026",
            "tax_period": "June",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-07-19T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2025-2026",
            "tax_period": "May",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-06-20T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2025-2026",
            "tax_period": "April",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-05-20T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2024-2025",
            "tax_period": "March",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-04-19T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR3B",
            "financial_year": "2024-2025",
            "tax_period": "February",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-03-20T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9",
            "financial_year": "2023-2024",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2024-12-30T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9",
            "financial_year": "2022-2023",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2023-12-30T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9",
            "financial_year": "2021-2022",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2023-02-15T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9",
            "financial_year": "2020-2021",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2022-02-26T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9",
            "financial_year": "2019-2020",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2021-03-31T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9",
            "financial_year": "2018-2019",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2020-12-31T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9",
            "financial_year": "2017-2018",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2019-07-30T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9C",
            "financial_year": "2023-2024",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2025-03-15T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9C",
            "financial_year": "2022-2023",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2024-02-06T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9C",
            "financial_year": "2021-2022",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2023-12-27T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9C",
            "financial_year": "2020-2021",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2022-02-28T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9C",
            "financial_year": "2019-2020",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2021-03-31T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9C",
            "financial_year": "2018-2019",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2021-01-02T00:00:00",
            "status": "Filed"
        },
        {
            "gstin": "",
            "filing_type": "GSTR9C",
            "financial_year": "2017-2018",
            "tax_period": "Annual",
            "tax_period_start_date": "",
            "tax_period_end_date": "",
            "filing_frequency": "",
            "date_of_filing": "2020-01-25T00:00:00",
            "status": "Filed"
        }
    ]
}

'''

state_code_map = {
    "01": "Jammu & Kashmir",
    "02": "Himachal Pradesh",
    "03": "Punjab",
    "04": "Chandigarh",
    "05": "Uttarakhand",
    "06": "Haryana",
    "07": "Delhi",
    "08": "Rajasthan",
    "09": "Uttar Pradesh",
    "10": "Bihar",
    "11": "Sikkim",
    "12": "Arunachal Pradesh",
    "13": "Nagaland",
    "14": "Manipur",
    "15": "Mizoram",
    "16": "Tripura",
    "17": "Meghalaya",
    "18": "Assam",
    "19": "West Bengal",
    "20": "Jharkhand",
    "21": "Odisha",
    "22": "Chhattisgarh",
    "23": "Madhya Pradesh",
    "24": "Gujarat",
    "26": "Dadra and Nagar Haveli and Daman and Diu",
    "27": "Maharashtra",
    "28": "Andhra Pradesh (Old)",
    "29": "Karnataka",
    "30": "Goa",
    "31": "Lakshadweep",
    "32": "Kerala",
    "33": "Tamil Nadu",
    "34": "Puducherry",
    "35": "Andaman & Nicobar Islands",
    "36": "Telangana",
    "37": "Andhra Pradesh (New)",
    "38": "Ladakh",
    "97": "Other Territory",
    "99": "Centre Jurisdiction"
}


def get_state_name(code):
    # Handles both integer (1) and string ("01") inputs
    str_code = str(code).zfill(2)
    return state_code_map.get(str_code, "Invalid Code")

def get_gst_info(gstin: str):
    data1 = get_gst_info_1(gstin)
    data2 = get_gst_info_2(gstin)
    
    # Extract the most reliable fields
    # Source 1 is usually better for Address/Legal Name
    # Source 2 is better for Filing history
    
    s1_data = data1.get("data", {})
    
    return {
        "gstin": gstin,
        "legal_name": data2.get("legal_business_name") or s1_data.get("lgnm"),
        "trade_name": data2.get("trade_name") or s1_data.get("tradeNam"),
        "status": data2.get("gstin_uin_status") or s1_data.get("sts") ,
        "constitution": s1_data.get("ctb") or data2.get("constitution_of_business"),
        # "principal_address": s1_data.get("pradr", {}).get("addr", {}),
        "state_code": gstin[:2],
        "state": get_state_name(gstin[:2]),
        "pan_number": gstin[2:12],
    }

if __name__ == "__main__":
    gstin = "07BLNPR7449R1ZT"
    gst_info = get_gst_info(gstin)
    print(gst_info)
from icecream import ic

DOMAIN = "franknguyenvd.au.auth0.com"
API_IDENTIFIER = "localhost:5000"
CLIENT_ID = "nDydbCaRbNAultiBLz5p9JxDGRSxhYIH"
CALLBACK_URI = "http://127.0.0.1:5000"
url = f"https://{DOMAIN}/authorize?audience={API_IDENTIFIER}&response_type=token&client_id={CLIENT_ID}&redirect_uri={CALLBACK_URI}"
ic(url)

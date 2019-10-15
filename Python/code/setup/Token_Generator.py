import requests
import json

pub_key = ''
priv_key = ''
Token = ''

def getNewToken():
    
    with open('C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\resources\\keys.json') as json_file:
        data = json.load(json_file)
        global pub_key
        pub_key = data['pub_Key']
        global priv_key
        priv_key = data['priv_Key']
            
    headers={"Content-type":"application/x-www-form-urlencoded"}
    access_token = requests.post(
            "https://api.tcgplayer.com/token",
            data={
                "grant_type": "client_credentials",
                "client_id": pub_key,
                "client_secret": priv_key,
            },
        )
    
    Json = json.loads(access_token.text)
    global Token
    Token = str(Json.get("access_token",""))

def getCurrentToken():
    if Token == '':
        getNewToken()
    return Token;

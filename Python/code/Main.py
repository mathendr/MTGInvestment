#import requests

#url = "http://api.tcgplayer.com/v1.32.0/app/authorize/authCode"
#url = "http://api.tcgplayer.com/v1.32.0/app/authorize/5134"
#url = "http://api.tcgplayer.com/v1.32.0/catalog/categories"
#response = requests.request("POST", url)

#print(response.text)

import requests
import json
import sys
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\code\\setup')
import Token_Generator
import ProductSetup
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\code\\products')
import getInformation
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\code\\save')
import writeToFile


skus = ProductSetup.getSkus()
product_name = ProductSetup.getProductNames()
group_id = ProductSetup.getGroupID()
product_id = ProductSetup.getProductID()
prices = []
headers = ProductSetup.getHeaders()


       
def getPrice():
    global prices
    prices = []
    count = 0
    for x in skus:
        url = "http://api.tcgplayer.com/v1.32.0/pricing/sku/" + str(x)
        auth_app = requests.get(url,headers = headers)

        Json = json.loads(auth_app.text)
        price = str(Json["results"][0]["marketPrice"])
        prices.append(price)
        print(price + " " + " " + (product_name[count]))
        count  = count +1
        
        

    
    
    
getInformation.getGroupId()
getInformation.getProductId(2418)
    
    





#getPrice()
#writeToFile.writeProductInfo(product_name,skus,group_id,product_id)
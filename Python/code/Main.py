#import requests

#url = "http://api.tcgplayer.com/v1.32.0/app/authorize/authCode"
#url = "http://api.tcgplayer.com/v1.32.0/app/authorize/5134"
#url = "http://api.tcgplayer.com/v1.32.0/catalog/categories"
#response = requests.request("POST", url)

#print(response.text)

import requests
import json
import sys
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\MTGInvestment\\Python\\code\\setup')
import Token_Generator
import ProductSetup
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\MTGInvestment\\Python\\code\\products')
import getInformation
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\MTGInvestment\\Python\\code\\save')
import writeToFile
import readFromFile


skus = ProductSetup.getSkus()
product_name = ProductSetup.getProductNames()
group_id = ProductSetup.getGroupID()
product_id = ProductSetup.getProductID()
prices = []
headers = ProductSetup.getHeaders()

        
def checkInvestment():
    inv = readFromFile.readInventory()
    
    profit = 0
    skus = []
    for x in inv:
        num = inv[x]["skus"]
        if num != -1:
            skus.append(num)
        
    priceData = getInformation.getPrice(skus)
    
    for x in priceData:
        priceSku = x["skuId"]
        mktPrice = x["marketPrice"]
        for y in inv:
            if inv[y]["skus"] != priceSku:
                continue
            else:
                inv[y]["current_value"] = mktPrice
                inv[y]["profit"] = float("{:.2f}".format((inv[y]["units"] * mktPrice) - (inv[y]["cost"]*inv[y]["units"])))
                profit = profit + inv[y]["profit"]
                
    print("${:.2f}".format(profit))
    writeToFile.updateInventory(inv)
#print()
#data = readFromFile.readProductSetup(getInformation.getGroupId())
#writeToFile.writeProductInfo(data)
#getPrice()

#data = getInformation.getPrice(skus)
#for x in data:
    #print(x["marketPrice"])
#getInformation.getProductId(2418)
    

checkInvestment()
#writeToFile.writeProductInfo(product_name,skus,group_id,product_id)
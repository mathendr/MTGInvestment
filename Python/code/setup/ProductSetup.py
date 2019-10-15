import requests
import json
import Token_Generator

skus = []
product_name = []
group_id = []
product_id = []

def getPrices():
    with open('C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\resources\\Product_Info.json') as json_file:
        data = json.load(json_file)
        for x in data:
            global product_name
            product_name.append(x)
            global skus
            skus.append(data[x]['skus'])
            global group_id
            group_id.append(data[x]['group_ID'])
            global product_id
            product_id.append(data[x]['product_ID'])

def getSkus():
    global skus
    if len(skus) == 0:
        getPrices()
    return skus

def getProductNames():
    global product_name
    if len(product_name) == 0:
        getPrices()
    return product_name

def getGroupID():
    global group_id
    if len(group_id) == 0:
        getPrices()
    return group_id
def getProductID():
    global product_id
    if len(product_id) == 0:
        getPrices()
    return product_id

def getHeaders():
    headers = {
        'Accept':'applications/json',
        'Authorization': "Bearer "+Token_Generator.getCurrentToken()
        }
    return headers
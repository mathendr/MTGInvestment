import requests
import json
import sys
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\code\\products')
import ProductSetup
import math
import string

headers = ProductSetup.getHeaders()
GroupInfo = []
ProductInfo = []


def getGroupId():
    respond = groupIdURLHelper(0)
    items = respond['totalItems']
    pages = math.ceil(int(items)/100) 
    data = []
    for x in range(0,pages):
        response = groupIdURLHelper(x*100)
        data = data +response['results']
    global GroupInfo
    GroupInfo = TrimGroupData(data)
    getAbreviationGroupID('WAR')
    
    
def getAbreviationGroupID(abrv):
    global GroupInfo
    if len(GroupInfo) == 0 :
        getGroupId()
    for x in GroupInfo:
        if str(x['abbreviation']).upper() == str(abrv).upper():
            return x
    return 'NONE'
   
def getProductId(groupID):
    url = "http://api.tcgplayer.com/v1.32.0/catalog/products"
    querystring = {"categoryId":"1","groupId":groupID,"includeSkus":'true', "limit":'100'}
    response = requests.get(url,headers = headers,params = querystring)
    data = json.loads(response.text)
    print(data['totalItems'])
    global ProductInfo
    ProductInfo = TrimProductData(data['results'])
    print(len(ProductInfo))
    print(ProductInfo)
    
    
    
    
def getSkus(groupID,productName):
    url = "http://api.tcgplayer.com/v1.32.0/catalog/products"
    querystring = {"categoryId":"1","groupId":groupID,"includeSkus":"true", "limit":"10000","productName": productName}
    auth_app = requests.get(url,headers = headers,params = querystring)
    Json = json.loads(auth_app.text)
    print(Json)
    

def groupIdURLHelper(offset):
    url = "http://api.tcgplayer.com/v1.32.0/catalog/groups"
    querystring = {"categoryId":"1","limit":'100','offset':offset}
    response = requests.get(url,headers = headers,params = querystring)
    return json.loads(response.text)


def TrimGroupData(data):
    for x in data:
        del x['isSupplemental']
        del x['publishedOn']
        del x['modifiedOn']
        if x['abbreviation'] == None:
            x['abbreviation'] = x['name']
    return data

def printShit():
    for x in GroupInfo:
        print(x['name'] + "   " + x['abbreviation'])
    
def TrimProductData(data):
    for x in data:
        del x['imageUrl']
        del x['url']
        del x['modifiedOn']
        newskus = []
        for y in x['skus']:
            if y != None:
                if y['languageId'] != 1:
                    del y
                elif y['conditionId'] !=6 and y['conditionId'] != 1:
                    del y
                else:
                    newskus.append(y)
        x['skus'] = newskus
    #print(data)
    return data
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
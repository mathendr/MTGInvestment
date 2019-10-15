import requests
import json
import sys
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\code\\products')
import ProductSetup



def writeProductInfo(product_name,skus,group_id,product_id):
    with open('C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\resources\\Product_Info.json','w') as json_file:
        count = 0
        data = {}
        for x in product_name:
            data[x] = {"skus":skus[count],"group_ID":group_id[count],"product_ID":product_id[count],"Extra":"extra3"}
            count = count +1
        
        json.dump(data,json_file)   
        
def updateInventory(product_name,date_purchased,cost,units,total_cost,current_price,profit):
    with open('C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\resources\\Inventory.json','w') as json_file:
        count = 0
        data = {}
        for x in product_name:
            data[x] = {"date_purchased":date_purchased[count],"cost":cost[count],"units":units[count],"total_cost":total_cost[count],"current_value":current_price[count],"profit":profit[count]}
            count = count +1
        
        json.dump(data,json_file)
    
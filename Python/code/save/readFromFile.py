import requests
import json
import sys

def readProductSetup(group_id):
    #print(group_id)
    finaldata = {}
    with open('C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\MTGInvestment\\Python\\resources\\Product_Info.json') as json_file:
        data = json.load(json_file)
        for x in data:
            group = data[x]['group_ID']
            for y in group_id:
                if y['groupId'] == group:
                    name = y['name']
                    finaldata[name] = data[x]
                    
        json_file.close()   
        return finaldata
            
         
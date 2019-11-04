import requests
import json
import sys
sys.path.insert(1,'C:\\Users\\Matthew\\Desktop\\MTGInvestment\\Python\\MTGInvestment\\Python\\code\\setup')
import Token_Generator
import ProductSetup
import MainMenu
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


MainMenu.start()
#MainMenu.getProductForInventory(2250,None)
#writeToFile.writeProductInfo(product_name,skus,group_id,product_id)
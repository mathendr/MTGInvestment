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

def start():
    mainMenu()
    try:
        ans = int(input("Number..."))
    
        if ans == 0:
            return
        if ans > 3 or ans < 0:
            print("out of range")
            printLines(3)
            start()

        if ans == 1:
            checkInvestment()
        elif ans == 2:
            checkInvestmentRefresh()
        elif ans == 3:
            addInventory()
            
    except ValueError:
        print("Please Enter a number...")
        printLines(3)
        start()

def mainMenu():
    print("Main Menu: ")
    print("Select Which Number to do....")
    print("1. Check Investment")
    print("2. Update Inventory Prices")
    print("3. Add To Inventory")
    print("0. Exit")
    

    
def checkInvestmentRefresh():
    inv = readFromFile.readInventory()
    
    profit = 0
    TotalInvestment = 0;
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
                TotalInvestment = TotalInvestment + float("{:.2f}".format((inv[y]["units"] * mktPrice)))
                
    writeToFile.updateInventory(inv)
    printLines(3)
    print("Prices Updated...")
    printLines(3)
    start()

def checkInvestment():
    inv = readFromFile.readInventory()
    profit = 0
    TotalInvestment = 0
    for y in inv:
        if(inv[y]["skus"] == -1):
            continue 
        profit = profit + inv[y]["profit"]
        TotalInvestment = TotalInvestment + float("{:.2f}".format((inv[y]["units"] * inv[y]["current_value"])))
    printLines(3)
    print("${:.2f} - Total Investment".format(TotalInvestment))
    print("${:.2f} - Current Profit/Loss".format(profit))
    printLines(3)
    start()

def addInventory():
    group = getInformation.getGroupId()
    lines = sorted(group, key=lambda k: k['publishedOn'], reverse = True)
    ans = input("Enter set name")
    printed = []
    count = 1
    for y in lines:
        if (ans.lower() in y["name"].lower()) or (ans.lower() in y["abbreviation"].lower()):
            print(str(count) + ". " + y["name"] + " " + y["abbreviation"])
            printed.append(y)
            count = count +1
    groupID = getLocationInArray(printed)["groupId"]
    getProductForInventory(groupID,None)
    
    #start()

def getProductForInventory(groupID,p):
    print(groupID)
    products = []
    if p is None:
        products = getInformation.getProductId(groupID)
    else:
        products = p
    printLines(3)
    printed = []
    count = 1
    for y in products:
        print(str(count) + ". " + y['cleanName'] + " " + str(y['skus'][0]['skuId']))
        printed.append(y)
        count = count +1
    selectedProduct = getLocationInArray(printed)
    
    if len(selectedProduct['skus']) > 1:
        #TODO: if the product has multiple skus
        print("Multiple Skus...Not Done Yet")
    
    print("You Selected....\n\n")
    print(selectedProduct['cleanName'])
    print("Is This Correct")
    if getans():
        printLines(3)
        getProductForInventory(groupID,products)
    else:
        print("You selected yes")
        
def getans():
    ans = str(input("(y/n)..").lower())
    if ans == "y":
        return False
    elif ans == "n":
        return True
    print("inccorect input try again..")
    getans()

def getLocationInArray(printed):
    try:
        ans = int(input("Which Item(0 to return)..."))
        if ans == 0:
            addInventory()
        elif ans < 0 or ans > len(printed):
            print("incorrect input")
            getGroupID()
        else:
            return printed[ans-1]
    except ValueError:
        print("please Input a Number")
        getGroupID(printed)
    
def printLines(num):
    for x in range(0,num):
        print(" ")
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
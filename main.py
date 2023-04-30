import csv
from fpdf import FPDF
def searchdata():
    findname = input("Enter your name to sarch name : ")
    with open(r'bills.csv', 'r+', newline='') as file:
        for line in file:
             if findname in line:
                searchline = line
    print(searchline)
def enterorder():
    global clientname
    while(1):
        clientname = input("Enter your name here to do order : ")
        if(clientname != ""):
            break
        else:
            print("please enter your name !")
    while(1):
        i=1
        for name,price in dishes.items():
            print(i,". "+name+" : ", price)
            i = 1+i
        dies = input("Enter dish number menu or enter 8 to exit: ")
        if (dies == ""):
            print("Enter any value or Enter 8 to Exit !")
        elif(int(dies) >= 9 ):
            print("\n\nplease enter valid option ! \n\n")
        else:
            if (int(dies) == i):
                break
            dicaname = list(list(dishes.keys())[int(dies)-1])
            que = int(input("Quantity for this iteam : " ))
            if ''.join([str(elem) for elem in dicaname]) in order.keys():
                order[''.join([str(elem) for elem in dicaname])] = str(int(order[''.join([str(elem) for elem in dicaname])])+que)
            else:
                order[''.join([str(elem) for elem in dicaname])] = str(que)
def storeorder():
    global datadishes ,total,clientname
    values = [clientname]
    for dicname,iteams in order.items():

        if datadishes ==  "":
            datadishes = dicname +" : "+iteams
        else:
            datadishes = datadishes + " , "+dicname +" : "+iteams
        total = dishes[dicname]*int(iteams) + total
    values.append(datadishes)
    values.append(total)   
    header = ['name', 'dishes and Quantity' ,' total bill']
    with open(r'bills.csv', 'r+', newline='') as file:
        DataList = file.readlines()
        csv_file = csv.writer(file)
        if not DataList:
            csv_file.writerow(header)
        csv_file.writerow(values)
def printpdf():
    global datadishes ,total,clientname
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    name = "Name : "+clientname
    diespdf = "list of dies : "+ datadishes
    totalpdf = "total of bill : "+ str(total)
    pdf.cell(200, 10, txt = name,ln = 1, align = 'c')
    pdf.cell(200, 10, txt = diespdf,ln = 1, align = 'c')
    pdf.cell(200, 10, txt = totalpdf,ln = 1, align = 'c')
    pdf.output(clientname+".pdf")
def afterorderoption():
    print("1. print pdf ")
    print("2. back to main manu")
    opstinafter = input("Enter option you to do : ")
    if(opstinafter == '1'):
        printpdf()
        afterorderoption()
    if(opstinafter == '2'):
        mainmanu()
def mainmanu(): 
    while(1):
        print("1. Enter you Order :  ")
        print("2. Search your order :  ")
        option = input("Enter what you want to do : ")
        if(option == '1'):
            enterorder()
            storeorder()
            afterorderoption()
        if(option == '2'):
            searchdata()
order = {}
dishes = {"Lemon rice" : 260,"Ghee rice" : 300,"Coconut rice":400,"Paneer Biryani":320,"Lucknowi Biryani" : 600,"Paneer butter masala ": 356,"Dal makhani": 600 }
clientname = ""
datadishes = ""
total = 0
mainmanu()
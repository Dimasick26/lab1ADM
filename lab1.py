import datetime
from modelsLab1 import *
import os


def createBD():
    isfile = False
    isfile = os.path.isfile('lab1.db')
    if (isfile == True):
        os.remove('lab1.db')
        with db:
            db.create_tables([Client, Order])
    else:
        with db:
            db.create_tables([Client, Order])
        isfile = True
    return isfile

def fillBD():
    isfile = False
    isfile = os.path.isfile('lab1.db')
    if (isfile == True):
        with db:
            clients = [
                {'Name':'Sophie','City':'San Francisco','Address':'123 Main Street'},
                {'Name':'Oliver','City':'New York','Address':'456 Oak Avenue'},
                {'Name':'Emma','City':'Paris','Address':'789 Maple Drive'},
                {'Name':'Liam','City':'London','Address':'1010 Elm Street'},
                {'Name':'Ava','City':'Sydney','Address':'1111 Pine Boulevard'},
                {'Name':'Noah','City':'Tokyo','Address':'2222 Cedar Lane'},
                {'Name':'Isabella','City':'Berlin','Address':'3333 Birch Road'},
                {'Name':'Ethan','City':'Toronto','Address':'4444 Willow Lane'},
                {'Name':'Charlotte','City':'Rio de Janeiro','Address':'5555 Oakwood Circle'},
                {'Name':'Mia','City':'Beijing','Address':'6666 Maple Street'}
            ]
            Client.insert_many(clients).execute()
            clientss = Client.select()
            orders = [
                {'Client_id':clientss[0],'Date':datetime.date(2022,2,15),'Amount':1.0,'Description':'Table'},
                {'Client_id':clientss[1],'Date':datetime.date(2023,1,17),'Amount':4.0,'Description':'Boad'},
                {'Client_id':clientss[2],'Date':datetime.date(2021,7,22),'Amount':7.0,'Description':'Cup'},
                {'Client_id':clientss[3],'Date':datetime.date(2022,10,21),'Amount':10.0,'Description':'Hammer'},
                {'Client_id':clientss[4],'Date':datetime.date(2022,6,9),'Amount':14.0,'Description':'Nails'},
                {'Client_id':clientss[5],'Date':datetime.date(2023,2,19),'Amount':6.0,'Description':'Chair'},
                {'Client_id':clientss[6],'Date':datetime.date(2023,2,10),'Amount':9.0,'Description':'Fastener'},
                {'Client_id':clientss[7],'Date':datetime.date(2022,12,5),'Amount':1.0,'Description':'Lamp'},
                {'Client_id':clientss[8],'Date':datetime.date(2022,2,17),'Amount':16.0,'Description':'Screw'},
                {'Client_id':clientss[9],'Date':datetime.date(2023,1,1),'Amount':22.0,'Description':'Boad'}
            ]
            Order.insert_many(orders).execute()
        CheckForTable = True
    else:
        print("Database does not exist!")
    return CheckForTable

def showClientsBD():
    isfile = False
    isfile = os.path.isfile('lab1.db')
    if (isfile == True):
        print(f"{'id' : <10}{'Name' : <15}{'City' : <15}{'Address' : <10}")
        for i in Client.select():
            print(f"{i.id : <10}{i.Name : <15}{i.City : <15}{i.Address : <10}")
    else:
        print("Database does not exist!")
    return Client.select().count()

def showOrdersBD():
    isfile = False
    isfile = os.path.isfile('lab1.db')
    if (isfile == True):
        print(f"{'id' : <10}{'Client_id' : <14}{'Date' : <16}{'Amount' : <10}{'Description' : <10}")
        for i in Order.select():
            print(f"{i.id : <10}{i.Client_id}\t\t{i.Date}\t{i.Amount : <10}{i.Description : <10}")
    else:
        print("Database does not exist!")
    return Order.select().count()

if __name__ == "__main__":     
    print("Choose an action\n1) initialize\n2) fill\n3) display TableName")
    task = input('Your choice: ')
    if (task == '1'):
        createBD()
         
    if (task == '2'):
        fillBD()
        
    if (task == 'show clients'):
        showClientsBD()

    if (task == 'show orders'):
        showOrdersBD()





from typing import List
import requests

#for status codes
from fastapi import status

#import classes
from Models.models import Client, Account, Transaction

BankApi_URL = "http://localhost:8000" 

def url(route: str):      
    return f"{BankApi_URL}{route}"

def print_Menu():
    print(""" 
          1: Add a client
          2: Add an account
          3: Get client's account 
          4: Get transactions made by an account
          5: Delete an account
          6: Update client's particulars
          7: Exit program
          """)


def add_client():
    print("add a client")
    client_id = input("client's id: ")
   
    if not str.isdigit(client_id):
        print("Please enter an integer id")
        return
    name = input("name: ")
    email = input ("email: ")
    telephone = input("telephone: ")
    
    client = Client(client_id= client_id, name=name, email=email,telephone=telephone)
    resp = requests.post(url("/clients"), json=client.dict())  
    if resp.status_code == status.HTTP_409_CONFLICT: 
        print ("A client with this id, already exists ")
        return
    if resp.status_code == status.HTTP_201_CREATED:
        print("The client is added")
        return
    print("----------------------")

def add_account():
    print("add an account")
     
    acc_numb = input("enter account number: ")
   
    if not str.isdigit(acc_numb):
        print("Please enter an integer id")
        return
    client_id = input("client's id: ")
    acc_type = input("enter the account's type: ")    

    new_account = Account(acc_numb= acc_numb, client_id= client_id, acc_type=acc_type)    
    resp = requests.post(url ("/accounts"), json=new_account.dict())  
    if  resp.status_code == status.HTTP_409_CONFLICT:
        print ("This account already exists")
        return
    if resp.status_code == status.HTTP_412_PRECONDITION_FAILED:
        print("The client does not exist")
        return
    if resp.status_code == status.HTTP_201_CREATED:
        print("Account added")
        return
    print("----------------")

def get_clients_accounts():
    print("Get client's accounts")
   
    client_id= input("please provide client's id: ")
    resp = requests.get(url(f"/clients/{client_id}/accounts"))
    
    if resp.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY:
        print("client's id must be an integer")
    if resp.status_code == status.HTTP_404_NOT_FOUND:
        print("No accounts were found for this id")
    if not resp.status_code == status.HTTP_200_OK:
        print("Try again")
        return
    data = resp.json()
    for Accounts in data: 
        Accounts = Account(**Accounts)
        print(f"acc_numb: {Accounts.acc_numb}")
        print(f"client_id: {Accounts.client_id}")
        print(f"acc_type: {Accounts.acc_type}")
        print("-------------------")
    
    
def get_transactions():
    print("get all the transaction made by an account number")

    acc_numb = input ("please enter the account number: ")
    resp = requests.get(url(f"/accounts/{acc_numb}/transactions"))
    if resp.status_code == status.HTTP_404_NOT_FOUND:
        print("No account found against this account number")    
    if not resp.status_code == status.HTTP_200_OK:
        print("Try again")
        return
    data = resp.json()
    for Transactions in data:
        Transactions = Transaction(**Transactions)
        print(f"trans_id: {Transactions.trans_id}")
        print(f"trans_date: {Transactions.trans_date}")
        print(f"trans_amount: {Transactions.trans_amount}")
        print(f"acc_numb: {Transactions.acc_numb}")
        print("---------------")
   

def delete_accounts():
    print("delete an account")      
    acc_numb = input("please enter the account number: ")
    
    resp = requests.delete(url(f"/accounts/{acc_numb}"))
    if resp.status_code == status.HTTP_404_NOT_FOUND:
        print("No account found against this account number")        
    else:
        print("account is deleted")   
    print("______________________")
   
def update_client():
    print("update clients particulars")
    client_id = input("client's id: ")
   
    if not str.isdigit(client_id):
        print("Please enter an integer id")
        return  
      
    name = input("name: ")
    email = input ("email: ")
    telephone = input("telephone: ")
    
    client = Client(client_id= client_id, name=name, email=email,telephone=telephone)
    resp = requests.put(url(f"/clients/{client_id}"), json=client.dict()) 
    if resp.status_code == status.HTTP_404_NOT_FOUND:
        print("the client with this id does not exist ")
        print("try again")
    else:
        print("successfully updated")  
   
      
def main():
    print_Menu()
    choice = input("please select your action: ")
    choice = choice.strip()
    if not str.isdigit(choice):
        print("Please enter a valid option")
        return

    match int(choice):
        case 1:
            add_client()
        case 2:
            add_account()
        case 3:
            get_clients_accounts()
        case 4:
            get_transactions()
        case 5: 
            delete_accounts()
        case 6:
            update_client()
        case 7:
            exit()                
        case _:
            print("Please enter a valid choice")


while __name__ == "__main__":
    main()


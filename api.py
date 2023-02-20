
##Accounts app
from datetime import date
from typing import List

from fastapi import FastAPI, Response, status

from config.database import BankDB
#import classes
from Models.models import Client, Account, Transaction

app = FastAPI()
database = BankDB("bank.db")

#base route
@app.get("/")
async def root():
    return "Welcome, to the Fast bank api"

#to get all the clients
@app.get ("/clients", tags=["clients"])
async def get_clients():
    data = database.get_clients()
    clients = []
    for element in data:
        client_id, name, email, telephone = element
        clients.append(Client(client_id = client_id, name = name, email = email, telephone = telephone))
    
    return (clients)

#to get the account of a particular client with their id
@app.get ("/clients/{client_id}", tags=["clients"])
async def get_client(client_id: int, resp: Response):
    data = database.get_client(client_id)
    if not data:
        resp.status_code = status.HTTP_404_NOT_FOUND
        return
    clients = []
    for element in data:
        client_id, name, email, telephone = element
        clients.append(Client(client_id = client_id, name = name, email = email, telephone = telephone))
    return (clients)


#to add a client
@app.post("/clients", status_code=status.HTTP_201_CREATED, tags=["clients"] )
async def post_add_client(client: Client, resp: Response):
    clientExists = database.get_client(client.client_id)
    if clientExists:
        resp.status_code = status.HTTP_409_CONFLICT
        return  
    data = database.add_client(client.client_id, client.name, client.email, client.telephone)   
    return True

#to update a client's particulars with client's id
@app.put ("/clients/{client_id}", tags=["clients"])
async def update_Client(client_id : int, client : Client, resp: Response):
    clientExists = database.get_client(client_id)
    if not clientExists:
        resp.status_code = status.HTTP_404_NOT_FOUND
        return    
    database.update_client(client.name, client.email, client.telephone, client_id)   
    return True

#get all accounts for a client
@app.get("/clients/{client_id}/accounts", tags=["clients"])
async def get_accounts(client_id: int, resp: Response ):    
    data = database.get_clients_accounts(client_id)
    if not data:
        resp.status_code = status.HTTP_404_NOT_FOUND
        return    
    accounts = []
    for element in data:
        acc_numb, client_id, acc_type = element
        accounts.append(Account(acc_numb=acc_numb, client_id =client_id, acc_type= acc_type))
    return (accounts)


#get account with acc_numb
@app.get("/accounts/{acc_numb}", tags=["accounts"])
async def get_account(acc_numb: int, resp: Response):
    data = database.get_account(acc_numb)
    if not data:
        resp.status_code = status.HTTP_404_NOT_FOUND
        return
    accounts = []
    for element in data:
        acc_numb, client_id, acc_type = element
        accounts.append(Account(acc_numb=acc_numb, client_id=client_id, acc_type=acc_type))
    return(accounts)

#to add an account
@app.post("/accounts", status_code=status.HTTP_201_CREATED, tags=["accounts"])
async def post_account(account: Account, resp: Response):
    accountExists = database.get_account(account.acc_numb)
    if accountExists:
        resp.status_code = status.HTTP_409_CONFLICT
        return
    clientsExists = database.get_client(account.client_id)
    if not clientsExists:
        resp.status_code = status.HTTP_412_PRECONDITION_FAILED
        return    
    data = database.add_account(account.acc_numb, account.client_id,account.acc_type)    
    return True

#to get the detail of transactions from a particular account with account number
@app.get ("/accounts/{acc_numb}/transactions", tags=["accounts"])
async def get_transactions(acc_numb: int, resp: Response):      
    data = database.get_transactions(acc_numb)  
    if not data:
        resp.status_code = status.HTTP_404_NOT_FOUND
        return
    transactions = []
    for element in data:
        trans_id, trans_date, trans_amount, acc_numb  = element
        transactions.append(Transaction(trans_id = trans_id,trans_date = trans_date, trans_amount= trans_amount,acc_numb=acc_numb ))
    return (transactions)

#to delete an account with account number
@app.delete ("/accounts/{acc_numb}", tags=["accounts"])
async def delete_account(acc_numb : int, resp: Response):
    accountExists = database.get_account(acc_numb)
    if not accountExists:
        resp.status_code = status.HTTP_404_NOT_FOUND
        return    
    data= database.delete_account(acc_numb)     
    if not data:
        resp.status_code = status.HTTP_404_NOT_FOUND
        resp.status_code = status.HTTP_200_OK     
        return
    return True
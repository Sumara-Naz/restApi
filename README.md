# Instructions to run this project
1. first run seed.py
2. run api.py
3. run Account app.py to execute program

## Following steps were followed to create this project

it is in a particular folder so to activate virtual environment run pipenv shell

1. ### installed packages
    - uvicorn
    - requests
    - fastapi

2. ### Created database
    folder | info
    ---    | ---
    Config |  contains database.py (createdtables in sqlite3 database stored with name AccountData
    Models | contains models.py file for classes
   
3. ### Create api.py

following end points are created
- GET /root
- GET /clients:to get all the clients
- GET /clients{client_id} : to geaspecific client
- GET /clients/{client_id}/accounts: togethe accounts against a specifclient id
- GET /accounts/{acc_numb}: to geallaccounts against an account number
- GET /accounts/{acc_numb}transactions: tget all thetransactions made by aaccount
- POST /clients : to add a client
- POST /accounts: to add an account
- DELETE /accounts/{acc_numb}: todelete aaccount with account number
- PUT /clients/{client_id}: to updataclient's particulars            

4. ### Create program Account_app.py

menu
 1. Add a client
 2. Add an account
 3. Get client's account 
 4. Get transactions made by anaccount
 5. Delete an account
 6. Update client's particulars
 7. Exit program

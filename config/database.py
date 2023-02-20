
import sqlite3
import os

class BankDB:
        database_url:str

        def __init__(self,database_url:str):
                self.database_url = database_url

                if not os.path.exists(self.database_url):
                   self.init_database()

        
        def call_database(self,query, *args):
                
                conn = sqlite3.connect(self.database_url)
                cur = conn.cursor()
                res = cur.execute(query,args)
                data = res.fetchall()
                cur.close()
                conn.commit()
                conn.close()
                return data


#create tables
        def init_database(self):

                init_database_clients = """
                CREATE TABLE IF NOT EXISTS Clients 
                (client_id INTEGER PRIMARY KEY,
                name TEXT NOT NULL, 
                email TEXT,
                telephone TEXT);"""
                
                init_database_accounts = """
                CREATE TABLE IF NOT EXISTS Accounts
                (acc_numb INTEGER PRIMARY KEY NOT NULL,
                client_id Integer, 
                acc_type TEXT,
                FOREIGN KEY (client_id)REFERENCES Client(client_id));""" 
                

                init_database_transactions = """
                CREATE TABLE IF NOT EXISTS Transactions
                (trans_id INTEGER PRIMARY KEY NOT NULL,       
                trans_date Date, 
                trans_amount FLOAT,
                acc_numb INTEGER ,
                FOREIGN KEY (acc_numb)
                REFERENCES Account(acc_numb));"""
                
                self.call_database(init_database_clients)                            
                self.call_database(init_database_accounts)                              
                self.call_database(init_database_transactions)  


        def get_clients(self):
                get_client_query = """
                SELECT * FROM Clients
                """
                return self.call_database(get_client_query)


        def get_client(self, client_id : int):    
                get_client_query = """    
                SELECT * FROM Clients WHERE client_id = ? 
                """
                return self.call_database(get_client_query, client_id) 
        

        def add_client(self, client_id, name, email, telephone):
                insert_client_query = """
                INSERT INTO Clients (client_id, name, email, telephone) 
                VALUES(?,?,?,?) 
                """
                self.call_database(insert_client_query, client_id, name, email, telephone)


        def update_client(self, client_id, name, email, telephone):
                update_client_query = """
                UPDATE Clients 
                SET name = ?, email = ?, telephone = ? 
                WHERE client_id = ? 
                """
                return self.call_database(update_client_query,name, email, telephone, client_id)


        def get_clients_accounts(self, client_id: int):
                get_account_query = """
                SELECT * FROM Accounts WHERE client_id = ?
                """
                return self.call_database(get_account_query, client_id)


        def get_account(self, acc_numb: int):
                get_account_query = """
                SELECT * FROM Accounts WHERE acc_numb = ?
                """
                return self.call_database(get_account_query, acc_numb)
        

        def add_account(self, acc_numb, client_id, acc_type):
                insert_account_query = """
                INSERT INTO Accounts(acc_numb, client_id, acc_type)
                VALUES(?,?,?)
                """
                return self.call_database(insert_account_query, acc_numb, client_id, acc_type)

                
        def get_transactions(self, acc_numb: int):
                get_transaction_query = """    
                SELECT * FROM Transactions WHERE acc_numb = ?   
                 """
                return self.call_database(get_transaction_query, acc_numb)


        def delete_account(self,acc_numb: int):
                delete_account_query = """
                DELETE FROM Accounts WHERE acc_numb = ?
                """
                return self.call_database(delete_account_query, acc_numb)

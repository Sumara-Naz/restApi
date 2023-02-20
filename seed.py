
import json
from config.database import BankDB

database = BankDB("bank.db")

create_Clients = """
INSERT OR IGNORE INTO Clients (
client_id,
name,
email,
telephone
) VALUES (
?, ?,?,?
) """

create_Accounts = """
INSERT OR IGNORE INTO Accounts (
acc_numb,
client_id,
acc_type)
 VALUES (
?, ?,? ) """

create_Transactions = """
INSERT OR IGNORE INTO Transactions (
trans_id,
trans_date,
trans_amount,
acc_numb )
VALUES (
?, ?,?,?) """

with open("seed.json", "r") as seed:
    data = json.load(seed)

    for client in data["Clients"]:
        database.call_database(create_Clients, client["client_id"], client["name"],
        client["email"], client["telephone"])

    for accounts in data["Accounts"]:
        database.call_database(create_Accounts, accounts["acc_numb"],accounts["client_id"],
        accounts["acc_type"])
    
    for transactions in data["Transactions"]:
        database.call_database(create_Transactions, transactions["trans_id"],transactions["trans_date"],
        transactions["trans_amount"],transactions["acc_numb"])

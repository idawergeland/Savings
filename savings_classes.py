import json

class Account:
    def __init__(self, id, account_number, account_type, balance, currency, owner):
        self.id = id
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.currency = currency
        self.owner = owner

    def update_balance(self, amount):
        # Update the account balance based on a transaction
        self.balance += amount

class Transaction:
    def __init__(self, id, date, description, amount, currency, account_id):
        self.id = id
        self.date = date
        self.description = description
        self.amount = amount
        self.currency = currency
        self.account_id = account_id

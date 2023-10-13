## Task description

Backend task:
I have used the account data and transaction data to get an overview of the accounts both before and after the transactions. 
In addition, I have set some individual goals for the accounts. If the account reaches the goal a congratulation will be printed. If not, the missing amount will appear.
Lastly, I've also added a rating in the end where the accounts are rated after their balance, and hopefully motivated to save more money to beat the others. This rating does not consider the individual goals.

## How to run

I have used the python-library, and to see the results you just need to run savings.py.
Additionally, you need the savings_classes.py, accounts.json and transactions.json files downloaded.

## Comments

Savings_classes.py contains an account-class and transation-class which is used to create the accounts and transactions in the savings.py-file.

Savings.py includes several functions to check the account balance, check goal status, and rate the accounts. 
Furthermore, the json-files (accounts and transactions) are loaded and list/dictionaries are created. 
Throughout the code I've added print-lines to present the result in the terminal.

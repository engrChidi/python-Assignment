
import sqlite3
conn = sqlite3.connect('bank.db')
print ("The DB is Created")

conn.execute('''CREATE TABLE BankAccount
         (AccountNumber INT PRIMARY KEY     NOT NULL,
         name           TEXT    NOT NULL,
         Phone            INT     NOT NULL,
         emailaddress        CHAR(50),
         balance         REAL);''')

print ("Accounts Table created")

#Autogenerate Account number for each New Account
def OpenAccount(Accnu, Name,Phone,Email, Amount):
            conn.execute(f"INSERT INTO BankAccount(AccountNumber, name,phone,emailaddress,balance) \
            VALUES (?, ?, ?, ?, ?)", (Accnu, Name, Phone, Email, Amount))
            conn.commit()
            print (Name, "\'s New Account Opened")

CustomerName = input("Your Name: ")
fon = int(input("Your Phone Number: "))
email = input("Email Adddress: ")
Amnt = float(input("Initial Deposit: "))
'''Auto Generate Account number'''
AcctNo = random.randint(1000000000,9999999999)
print('\n---------- New Account Found -----------\n')
OpenAccount(AcctNo, CustomerName, fon, email, Amnt)
print('\n------------ Database closed ------------')

def viewCustomerList():
    cursor = conn.execute("SELECT rowid, AccountNumber, name, phone, emailaddress, balance from BankAccount")
    for row in cursor:
                    print ("SN = ", row[0])
                    print ("Account-Number = ", row[1])
                    print ("Customer-Name = ", row[2])
                    print ("Phone Number = ", row[3])
                    print ("Email Address = ", row[4])
                    print ("Balance = ", row[5], "\n")
    conn.close()
    
viewCustomerList()
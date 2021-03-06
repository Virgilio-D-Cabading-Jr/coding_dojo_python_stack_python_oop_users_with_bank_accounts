# //////////////////////////////////////////////////////////
# Subj: Coding Dojo > Python Stack > Python > OOP: Users with Bank Accounts 
# By: Virgilio D. Cabading Jr
# //////////////////////////////////////////////////////////

import utl

# //// BANK ACCOUNT CLASS //////////////////////////////////

class BankAccount:
    all_accounts = []

    def __init__(self, int_rate=10, balance=0):                 # Construct an instance of the bank account class
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        self.account_num = len(BankAccount.all_accounts)

    def deposit(self, amount):                                  # Add amount to the bank account balance
        self.balance += amount
        return self

    def withdraw(self, amount):                                 # Subtract amount from the bank account
        if (self.balance-amount) >= 0:                          # if Account has sufficient balance, withdraw the amount requested
            self.balance -= amount
        else:                                                   # if there is insuficient balance, withdraw the amount and charge 5
            print(f"{f'Insufficient funds to withdraw ${amount} from account balance of ${self.balance} ':*<100}")
            self.balance -= (5 + amount)
            print(f"{f'Charging $5 due to insufficient balance, new account balance is ${self.balance} ':*<100}\n")
        return self
    
    def display_account_info(self):
        print(f'account # : {self.account_num} ::: balance : ${self.balance} ::: interest rate : {self.int_rate}% ')
        return self

    def yield_interest(self):
        interest_gained = self.balance * (self.int_rate / 100)  # calculate the interest gained
        self.balance+= round(interest_gained,2)                 # add the interest gained to the account balance rounded to 2 decimal points
        return self

    @classmethod
    def print_all_account_info (cls):                           # print info on all existing bank accounts
        utl.print_desc_center("Information on All Bank Accounts")
        for account in cls.all_accounts:
            account.display_account_info()
        print()

# //// USER CLASS //////////////////////////////////////////

class User:

    # **** CLASS METHODS **********************************
    def __init__(self, first_name = "John", last_name = "Doe") -> None:     # Class Instance Constructor
        self.first_name = first_name                                        
        self.last_name = last_name
        self.account = []                                       # Create a list of accounts with an initial single account
        self.account.append(BankAccount(2,0))

    def make_deposit (self, account_idx, amount):                   # Method that increases the user's account balance by amount
        self.account[account_idx].deposit(amount)
        return self

    def make_withdrawal (self, account_idx, amount):                     # Method that decreases the user's account_balance by specified amount
        self.account[account_idx].withdraw(amount)
        return self
    
    def display_user_balance(self):                         # Method display user balance
        print(f"{f' User Balance ::: First Name : {self.first_name} :: Last Name : {self.last_name} ':*^100}")
        for account in self.account:
            account.display_account_info()
        return self

    def add_bank_account (self, int_rate, amount):
        self.account.append(BankAccount(int_rate, amount))
        return self
    
    # def transfer_money (self, other_user, amount):     # Method to transfer an amount from user to another user
    #     self.make_withdrawal(amount)
    #     other_user.make_deposit(amount)
    #     return self

    def info(self):                                         # Method that displays info of class instance
        print(f"{f' User ::: First Name : {self.first_name} :: Last Name : {self.last_name} ':*^100}")
        for account in self.account:
            account.display_account_info()
        # print(f"account_balance: {self.account_balance}\n")
        return self

# //// FUNCTIONS ///////////////////////////////////////////

# //// MAIN EXECUTABLE SECTION /////////////////////////////

user_1 = User("Vin", "Diesel")                                      # 3 users created
user_2 = User("Brad","Pitt")
user_3 = User("Dwayne","Johnson")

user_1.make_deposit(0,10000).display_user_balance()                                 # the 3 users make their initial deposits
user_2.make_deposit(0,25000).display_user_balance()
user_3.make_deposit(0,50000).display_user_balance()

print()
utl.print_desc("Vin got hungry, so he bought a $7 in and out burger")
user_1.make_withdrawal(0,7).display_user_balance()
print()

utl.print_desc("The Rock makes bank in his new movie Fast and Furiouser, so he opens another bank account")
user_3.add_bank_account(5,1234567).display_user_balance()
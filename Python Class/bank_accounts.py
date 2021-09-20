################################################################################
# Author: Miguel Castilho Oliveira
# Date: 04/22/2021
# Description calculates balance in a bank account. It uses the conceptof class to create an instance of a specific bank account and its balance
################################################################################
class Account():
    def __init__(self, balance): #defining the atributte
        self.balance = balance
        print(f'New account balance: ${self.balance:0.2f}')
        
    def deposit(self, amount): #deposit method
        print(f"Deposit: ${amount:0.2f}")
        self.balance += amount
        
    def withdraw(self, amount): #Withdraw method
        
        if amount <= self.balance:
            print(f"Withdraw: ${amount:0.2f}")
            self.balance -= amount
        
        else:
            print(f"Withdraw: ${amount:0.2f}")
            print("Insufficient funds. Withdrawal canceled.")
        
    def get_balance(self): #method to chekc the balance
        print(f'Balance: ${self.balance:0.2f}')

class Savings(Account):
    
    def __init__(self, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(balance)
        
    def accrue_interest(self):
        intPayment = self.balance * self.interest_rate
        self.balance += intPayment
        print(f"Interest payment: ${intPayment:0.2f}")
                  
    
def main():
    theBalance = Savings(200, 0.1)
    theBalance.get_balance()
    theBalance.deposit(12.34)
    theBalance.get_balance()
    theBalance.withdraw(40)
    theBalance.get_balance()
    theBalance.withdraw(200)
    theBalance.get_balance()
    theBalance.accrue_interest()
    theBalance.accrue_interest()
    theBalance.accrue_interest()
    theBalance.withdraw(200)
    theBalance.get_balance()
    
if __name__ == '__main__':
    main()

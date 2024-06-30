




class Account:
   
    def __init__(self,balance,accontPin):
        self.balance = balance
        self.accounNo = accontPin
     

    def Debit(self,amount):
        self.balance -= amount
        print(f"RS. {amount} was debited")
        print(f"Total amount after debit is {self.printBalance()}")

    def Credit(self,amount):
        self.balance += amount
        print(f"RS. {amount} was credited")
        print(f"Total amount after credit is {self.printBalance()}")

    def printBalance(self):
        return self.balance

acc1 = Account(78945,2050);
# acc1.Credit(200)
acc1.Debit(50000)



        
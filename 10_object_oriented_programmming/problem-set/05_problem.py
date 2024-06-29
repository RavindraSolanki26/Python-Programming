
import random


class Train:
    
    def __init__(self,trainNo):
        self.trainNo = trainNo

    def Book(self,fro,to):
        print(f"Your ticket in TrainNo {self.trainNo} is Booked from {fro} to {to}")    
    

    def getStatus(self):
        print(f"Train No: {self.trainNo} is running on time")

    def getFare(self , fro,to):
        print(f"Ticket fare in train no {self.trainNo} from {fro} to {to} is {random.randint(222,5555)}")
t = Train(123555)    
t.Book("jaipur","Delhi") 
t.getStatus();
t.getFare("jaipur","Delhi")   
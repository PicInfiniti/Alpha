from DataBase import *
from os import system

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.Namads = {}
        
    def OrderSend(self, PR, aggressive):
        pass
        
def Print(a):
    t = ""
    for i in a.keys():
        t+=id2stock(i,2)+": "+str(a[i][0])+" "+str(a[i][1])+"\n"
        
    system("clear")
    print(t)
        
def BEY(PV, SR, FV=1000000):
    return (FV/PV-1)*(365/SR)
    

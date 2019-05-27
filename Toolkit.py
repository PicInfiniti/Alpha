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
        ask = str(a[i][2])
        if int(ask) != 0: ask = str(BEY(ask, a[i][0]))
        bid = str(a[i][3])
        if int(bid) != 0: bid = str(BEY(bid, a[i][0]))
        t += id2stock(i,2) + ": " + str(a[i][0]) + " " + str(a[i][1]) + " " + ask + " " + bid+"\n"
    system("clear")
    print("Namad\t Sr BEY\t\t\tBEYask\t\t    BEYbid")
    print(t)
        
def BEY(PV, SR, FV=1000000):
    return (FV/int(PV)-1)*(365/SR)

def MaxDic(Dic, t=1):
    return max([Dic[i][t] for i in Dic.keys()])
    



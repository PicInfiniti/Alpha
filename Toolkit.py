from DataBase import *
from os import system

class Account:
    def __init__(self, balance):
        self.balance = balance
        self.asset = {}
        self.orders = {}
    
    def Order(self,Dic ,bey):
        if not self.balance:
            return
            
        ask = MaxDic(Dic, 2)
        bid = MaxDic(Dic, 3)
        if BEY(bid[1], Dic[bid[0]][0]) > bey:
            self.orders[bid[0]] = bid[1]
            self.balance -=self.balance
            return
        
        elif BEY(ask[1]+1, Dic[ask[0]][0]) > bey:
            self.orders[ask[0]] = ask[1]+1
            self.balance -=self.balance
            return        
        
        else:
            for i in Dic.keys():
                self.orders[i] = int(BEY(False, Dic[i][0], bey))
            
    
    def OrderSend(self):
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
        
def BEY(PV, SR, bey=False, FV=1000000):
    if bey: return 365*FV/(SR*bey+365)
    return (FV/int(PV)-1)*(365/SR)

def MaxDic(Dic, t=1):
    Max = [0, 0]
    for i in Dic.keys():
        if Dic[i][t] > Max[1]: Max = [i, Dic[i][t]]
        
    return Max
    



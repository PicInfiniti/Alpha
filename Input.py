Input = {"strategy": "buy",
        "Balance" : 1000000000,
        "SarResid" : [50, 100],
        "maxweight" : .1,
        "aggressive" : .23,
        "PR" : .005,
        }
        
class Account():
    def __init__(self, balance):
        self.balance = balance
        self.Namads = {}
        
    def OrderSend(self, PR, aggressive):
        pass

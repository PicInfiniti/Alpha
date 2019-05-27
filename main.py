import jdatetime as jdt
from Input import Input
from Toolkit import *
from time import sleep
#{Code:[SR, Hajm, Close, Payani, ask, bid]}
account = Account(Input["balance"])

with open("namad.csv") as namads:
    Namads = {}
    for i in namads.read().split():
        hv = i.split(",")#help variable
        today = jdt.datetime.now().date()
        Delta = (jdt.datetime.strptime(hv[1],"%Y.%m.%d").date()-today).days
        Namads[hv[0]] = Delta
        
DB = 'StockData.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
while True:
    sleep(1)

    try:
        with open("Input.py") as Input:
            Input = Input.read()
            exec(Input)
            Filter = {}
            for i in Namads.keys():
                if Input["SarResid"][0]<Namads[i]<Input["SarResid"][1]:
                    AB = Online(i) #ask, bid
                    Filter[i] = [Namads[i], 0 , int(AB[0]), int(AB[1])]
        UpdateDB()
    except:
        continue

    # extract all stock name stored in database ans store to List
    cursor.execute('''
                    SELECT
                        Code, Hajm, Close, Payani
                    FROM
                        StockInfo
                    WHERE
                        Code in Namad'''.replace("Namad",str(tuple(Filter.keys()))))
    List = cursor.fetchall()

    #add BEY
    for i in List :
        SR = Filter[i[0]][0]
        PV = int([i[2],i[3]][int(i[1])==0])
        Filter[i[0]][1] = BEY(PV, SR)

    Print(Filter)
    wbey = MaxDic(Filter)[1]+Input["PR"]
    print("MBEY+"+str(Input["PR"])+":", wbey,"\n")

    account.Order(Filter, wbey)
    account.OrderSend()
    for i in account.orders.keys():
        print(id2stock(i,2), account.orders[i] )



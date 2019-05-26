import jdatetime as jdt
from DataBase import *
from Input import Input
from time import sleep
from os import system
#{Code:[SR, Hajm, Close, Payani]}

def Print(a):
    for i in a.keys():
        print(id2stock(i,2),": ",a[i][0], a[i][1])
        
with open("namad.csv") as namads:
    Namads = {}
    for i in namads.read().split():
        hv = i.split(",")#help variable
        today = jdt.datetime.now().date()
        Delta = (jdt.datetime.strptime(hv[1],"%Y.%m.%d").date()-today).days
        if Input["SarResid"][0]<Delta<Input["SarResid"][1]:
            Namads[hv[0]] = [Delta, 0]

def BEY(PV, SR, FV=1000000):
    return (FV/PV-1)*(365/SR)

DB = 'StockData.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()
while True:

    sleep(1)
    try:
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
                        Code in Namad'''.replace("Namad",str(tuple(Namads.keys()))))
    List = cursor.fetchall()

    #add BEY
    for i in List :
        SR = Namads[i[0]][0]
        PV = int([i[2],i[3]][int(i[1])==0])

        if int(i[1]): Namads[i[0]][1] = BEY(PV, SR)

    system("clear")
    Print(Namads)




import jdatetime as jdt
from DataBase import *
from Input import Input
import numpy as np

#{Code:[SR, Hajm, Close, Payani]}

with open("namad.csv") as namads:
    Namads = {}
    for i in namads.read().split():
        hv = i.split(",")#help variable
        today = jdt.datetime.now().date()
        Namads[hv[0]] = [(jdt.datetime.strptime(hv[1],"%Y.%m.%d").date()-today).days]

def BEY(PV, SR, FV=1000000):
    return (FV/PV-1)*(365/SR)

DB = 'StockData.db'
conn = sqlite3.connect(DB)
cursor = conn.cursor()

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
    if int(i[1]):
        Namads[i[0]].append(BEY(PV, SR))
        






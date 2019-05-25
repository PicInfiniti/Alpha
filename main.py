import jdatetime as jdt
from Input import Input

def BEY(PV, SR, FV=1000000):
    return (FV/PV-1)*(365/SR)

with open("namad.csv") as namads:
    Namads = {}
    for i in namads.read().split():
        hv = i.split(",")#help variable
        today = jdt.datetime.now().date()
        Namads[hv[0]] = [(jdt.datetime.strptime(hv[1],"%Y.%m.%d").date()-today).days]



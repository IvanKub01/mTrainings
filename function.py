import re
from datetime import date, datetime, timedelta
import time
def sqlcondition(prem1,prem2,prem3,prem4,prem5):
    selects = { "OsobneCislo " : prem1,
                "PlanTyz" : prem2 ,
                "zod.Nazov " : prem3,
                "skol.Nazov " : prem4,
                "skolpoz.Nazov " : prem5             
                ,}

    SQLselect = ""

    for i,j in selects.items():
        if j!='':
            SQLselect += " AND "+i+" = '"+j+"'"


    return SQLselect

def eatSpace(valuePar):
    MyString =""
    MyString = valuePar
    MyString = re.sub("^\\s+|\\s+$", "", MyString, flags=re.UNICODE)
    return MyString
def changeval(valuePar):
    val = valuePar
    val = str(val.strftime("%d.%m.%Y %H:%M:%S"))
    val = val[:-3]
    return val
def shorttime(valuePar):
    val = valuePar

    val = val[0:5]
    return val
def makeDateTime(valueDate):
    if(valueDate != ""):
    
        valueDate = datetime.strptime(valueDate, "%Y-%m-%d")
        valueDate = str(valueDate)

        MyString = ""
        MyString = " AND datediff(minute,term.DatumSkolenia, '" + valueDate + "' ) = 0"
     
 
    return MyString
def makeDateTimeFromInput(valueD):

    Mystring = ""
    ii = int(valueD[11:13])

    if(ii >= 13):

        ii -= 12
        ii = str(ii)
        Mystring = valueD[0:4] + valueD[5:7] + valueD[8:10] + " " +  ii +  valueD[13:16] + ":00 PM"

    else:
        
        Mystring = valueD[0:4] + valueD[5:7] + valueD[8:10] + " " + valueD[11:16] + ":00 AM"
    
    return Mystring

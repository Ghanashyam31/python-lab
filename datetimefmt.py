from datetime import datetime,date,time,timedelta

def showdate():
    newDtTm = datetime.now().strftime("Todays date %A, %d %B %Y and Time %H:%M:%S %p")
    return newDtTm

def yeardays():
    msgString=''
    yearLastDay = date(2020,12,31)
    currentDay = date.today()
    dysPassed = datetime.now().strftime("%j")
    nxtYear = int(datetime.now().strftime("%Y"))
    nxtYear+=1
    nwYearDays = (yearLastDay-currentDay).days
    msgString =  "Till date " + str(dysPassed) + " days elapsed for year and " + str(nwYearDays) + " days are remaning for new year (" + str(nxtYear) + ")." 
    return msgString

# def sampleFun():
#     global g 
#     g='AAA'
#     a = 5
#     b = 10
#     total = a + b
#     return a,b,total

# intVar = sampleFun()
# print(intVar[2], g)



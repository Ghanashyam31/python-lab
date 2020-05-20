from datetime import datetime,date,time,timedelta
import calendar
#idt=input("Enter your Birth Date in specified format (DD/MM/YYYY):")
#bdt=datetime.datetime.strptime(idt,'%Y,%m,%d').date
 
def show_birthdate(bdt,nlst):
    maxMonthDy=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    leapYear=[1904,1908,1912,1916,1920,1924,1928,1932,1936,1940,1944,1948,1952,1956,1960,1964,1968,1972,1976,1980,1984,1988,1992,1996,2000,2004,2008,2012,2016,2020,2024,2028,2032,2036,2040,2044,2048,2052,2056,2060,2064,2068,2072,2076,2080,2084,2088,2092,2096]
    #weekLst=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    ## WeekName list populating ...
    weekLst=str(calendar.weekheader(12)).split()
    currentDt=date.today()
    i=0

    #Extracted the current day, month and year 
    currentDay=int(datetime.now().strftime("%d"))
    currentMonth=int(datetime.now().strftime("%m"))
    currentYear=int(datetime.now().strftime("%Y"))

    for idt in bdt:
        #Spliting the birth date 
        bdtStr=idt.split('/')

        #Storing day,month and year separatly to different variables
        dt=int(bdtStr[0].lstrip('0'))
        mt=int(bdtStr[1].lstrip('0'))
        yr=int(bdtStr[2])

        leapYr = yr
        #Calculating leap year days for difference days to adjustments
        if leapYr not in leapYear:
            for j in range(3):
                if leapYr in leapYear:
                    findleapYr = leapYr
                else:
                    leapYr+=1
            leapYearDys=(leapYear.index(currentYear)-leapYear.index(findleapYr))+1
        else:
            leapYearDys=(leapYear.index(currentYear)-leapYear.index(yr))+1

        #Birth date Days calculations 
        #birthDt=date(currentYear,currentMonth,1)
        #birthDays=(currentDt-birthDt).days
        #bDt=date(currentYear,mt,dt)
        birthDt=date(currentYear,currentMonth,1)
        birthDays=(currentDt-birthDt).days
        startingMonthDys=maxMonthDy[mt]-dt
        if startingMonthDys in [30,31]: startingMonthDys=0
        totalDys=startingMonthDys+birthDays+leapYearDys

        #Birth date Month calculations 
        if mt == currentMonth:
            actualMonths=0
        elif mt < currentMonth:
            actualMonths=currentMonth-1            
        else:
            bMonthNo1=12-int(mt)
            bMonthNo2=currentMonth-1
            actualMonths=bMonthNo1+bMonthNo2

        #Birth date Year calculations 
        birthYear=currentYear-yr
        #print("Your age as per your Birth Date (", idt,") is:", birthYear, "Years", actualMonths , "Month and ", birthDays , " Days..." )
        #bStr = str(nlst[i]).capitalize() + " your age as per your Birth Date ("+ str(idt) + ") is:"+ str(birthYear) + " Years " +  str(actualMonths) + " Month and " + str(birthDays) + " Days..."
        #return bStr
        birthD=(calendar.weekday(yr,mt,dt))
        print("{0:>12s} your age as per your Birth Date {1:12s} is {2:3d} Years {3:3d} Month and {4:3d} Days ... Your Birth Day is {5:13s}".format(str(nlst[i]).capitalize(),str(idt),birthYear,actualMonths,totalDys,weekLst[int(birthD)]))
        i+=1
    
    return

#Calculatung the days remaining to birth day
#bDt=(bDt-currentDt).days
#if int(bDt) < 1:
#    print("Your Birth already passed", bDt, " days ago....")
#else:
#    print(bDt, "Days are remaining to your Birth day....")

Bdatelst=["18/08/1972","31/05/1976","10/05/1978","17/10/2005","04/08/2010","28/03/1999","08/03/2002"]
Namelst=["Naresh","Ghanashyam","Mahesh","Devendra","Angad","Gauri","Dhananjay"]
show_birthdate(Bdatelst,Namelst)

#for st in lst:
#    print(st)
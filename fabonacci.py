from datetime import datetime
import random

print("Current date and Time",datetime.now().strftime("%A, %d %B %Y"))

list1=[]
a=0
b=1
c=0
#print("Fac no:",0)
#print("Fac no:",b)
list1.append(0)
list1.append(1)

for x in range(1,8,1):
    add = a + b
    #print("Fac no:",add)
    list1.append(add)
    c=add
    a=b
    b=c

for i in range(len(list1)):
    print("Array Index No:", i , "Fabonacci No:", list1[i])

print("Random no :",random.randrange(1,10))
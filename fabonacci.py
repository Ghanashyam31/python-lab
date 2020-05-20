from datetime import datetime
import random
import re

listTwo=['1. "Do not dwell in the past, do not dream of the future, concentrate the mind on the present moment."',
'2. "The trouble is, you think you have time."',
'3. "Happiness will never come to those who fail to appreciate what they already have."',
'4. "We are what we think. All that we are arises with our thoughts. With our thoughts, we make the world."',
'5. "Every morning we are born again. What we do today is what matters most."',
'6. "Train your mind to see something good in everything." ',
'7. "If you light a lamp for somebody, it will also brighten your path." ',
'8. "The quieter you become, the more you can hear."',
'9. "You will not be punished for your anger, you will be punished by your anger.',
'10. "Your worst enemy cannot harm you as much as your own unguarded thoughts."',
'11. "With our thoughts, we make the world." ',
'12. "No matter how hard the past, you can always begin."',
'13. "You only lose what you cling to."',
'14. "Rule your mind or it will rule you."',
'15. "Let the past make you better, not  bitter."',
'16. "The root of suffering is attachment." ']

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
    #c=add
    a=b
    b=add

for i in range(len(list1)):
    print("Array Index No:", i , "Fabonacci No:", list1[i])

print("Random no :",random.randrange(1,10))

str1=str(random.choice(listTwo)).split('.')
#print(str1[0])
print("Buddha Quqotes :")
print(str1[1][2:])
print("Deeper the Creving, Deeper is the Aversion", "Deeper the Aversion, Deeper is the Affiction !!!")

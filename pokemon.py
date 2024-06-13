''' python code to train pokemon 
powers = [3, 8, 9, 7] 
   
mini, maxi = 0, 0
   
for power in powers: 
    if mini == 0 and maxi == 0: 
        mini, maxi = powers[0], powers[0] 
        print(mini, maxi) 
    else: git

        mini = min(mini, power) 
        maxi = max(maxi, power) 
        print(mini, maxi) '''
 #IDENTIFIER
 #1.IDENTIFIER IS THE NAME OF A VARIABLE 
 #identifier can be combination of lower caser upper case letter
 #it can not starts with digit
 #we can not use special character like @,# etc
 #identifier can be any length
#the variable name should be any length
#variable should have proprer meaning
#type()-used to show the datatyape of avariable

'''name="ashok"
age=12
print(type(name))
print(type(age))'''

#DATATYPE
#mainly data type s are 5 iltype in python
#-integer
#string
#float
#boolean
#none-not assingn

#print sum of two number
'''a=12
b=12
sum=a+b
print("sum of a and b is",sum)#24'''
a=5
b=3
'''print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a/b)
print(a//b)
print(a**b)'''

#relational
'''print(a=b)
print(a<b)
print(a>b)'''
'''num=10
num=num+10
print(num)'''
'''val1=True
val2=False
print(val1 and val2)
print(val1 or val2)'''
name=(input("enter your name"))
age=input("enter your age")
print(name)
print(age)


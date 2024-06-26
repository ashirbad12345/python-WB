'''print("hellow world")
def sum_of_integer(n1,n2):
          sum=n1+n2
          return sum

x=int(input("enter the first number"))
y=int(input("enter the second number"))
ans=sum_of_integer(x,y)
print(ans)'''
#arbitary argument
def addAllNumber(*args):
    sum=0
    for i in args:
        sum+=i
        return sum
    
output=addAllNumber(2,3,4,5,6)   
print(output) 



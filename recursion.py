'''def factorial(n):
    
    if n==0:
        return 1
    fact=n*factorial(n-1)
    return fact
n=int(input("enter the  number:"))
print("facorial is:",factorial(n))'''
#find power of a number
'''def power(a,b):
    if b==0:
        return 1
    ans=a*power(a,b-1)
    return ans

a=int(input("enter value of a:"))  
b=int(input("enter value of b:"))  
print("power of the number is :",power(a,b))'''


#write a programe to print numbers from n to 1
'''def print_n_to_1(n):
    #base case
    if n==0:
        return 
    print(n)
    print_n_to_1(n-1)
n=int(input("enter the number:"))    
(print_n_to_1(n))''' 

#print number froom 1 t0 n
'''def print_1_to_n(n):
    #base case
    if n==0:
        return 
    print_1_to_n(n-1)
    print(n)
    
n=int(input("enter the number:"))    
print_1_to_n(n) '''

#print the fabonacci series
def fibonacci(n):
    #base case
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        
            return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("enter the number:")) 
for i in range(1,n+1):   
       print(fibonacci(i))    
        

    
            


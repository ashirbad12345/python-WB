#rectangular pattern
'''n=int(input("enter the range"))
for i in range(n):
    print("*"*10)'''

#rectangular number printing
'''n=int(input("enter the range:"))
for i in range(n):
    for j in range(1,n+1):
        print(j,end=" ") 
    print()'''


# one sided pyramid pattern
n=int(input("enter the range"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")

    print()    


 
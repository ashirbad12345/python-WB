def add_numbers_recurcive(x,y):
    if y==0:
         return x
    else:
         return add_numbers_recursive(x+1,y-1)
    num1=4
    num2=10
    result=add_numbers_recursive(num1,num2)
    print("sum of",num1,"and",num2,"is",result)
'''str="ashirbad"
print(str)
print(str[0])
print(str[0:5])
print(str[0:8:2])
print(str[::-1])
print(str.upper())
print(str.lower())
print(str.capitalize())
str2="bapun"
str3=str+str2
print(str3)
print(str3.replace("bapun","ash"))
str4="hello Ashirbad"
print(str4)
print(str4.strip())
print(str4.split())'''

#write a python function that checks if the given string is a pallindrom or not
def check_string(str):
    reverse_string=str[::-1]
    return check_string==str
str=input("enter the string:")
if check_string(str):
    print("the string is pllindrom")

else:
    print("the string is not pallindrom")    
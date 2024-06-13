#creating the dictionary
'''phones={
    "ashirbad":8458015796,
    "saty":9178032949,
    "pintu":912509379,
    "subham":9223444
}
print(phones)
#type of phones
print(type(phones))
#length of the dictionary
print(len(phones))

#accessing item of a list
#print(phones["ashirbad"])
#accessing item using get()function
#print(phones.get("saty"))
#ACCESSING ALL THE KEY OF DICTIONARY
#print(phones.keys())

#upadate value of a key in a dictionary
phones["ashirbad"]=11111111111
print(phones)

#add element of a list
phones["rahul"]=2222222
print(phones)

#ADD ANOTHER DICTIONARY 

    #print(x)
#TO PRINT THE VALUE OF KEY OF A DICTIONARY    
''#'for i in phones:
    print(phones[x])  
#FOR PRINT KEYS AND VALUES OF ADICTIONARY AT A TIME
#for x in phones.items():
   # print(x)  
#FOR PRINT KEYS AND VALUES OF ADICTIONARY AT A TIME DISTINCTLY
#for x,y in phones.items():
    #print(x,y)

#NESTED DICTIONARY
area={
    "area1":{
        "a":1,
        "b":2,
        "c":3
    },
    "area2":{
        "x":4,
        "y":5,
        "z":6
    }
} 
print(area["area1"]["a"])
print(area["area2"]["x"])
print(area["area1"]["b"])
print(area["area2"]["y"])
 
 #print sum of the dictionary values
'''dict={
    "a":100,
    "b":200,
    "c":300
}
print(dict.values())
print("the sum of the values of dictionary is:",sum(dict.values()))'''

'''zip()=this function can add two list to a dictionary in which values of first list contain
the key  and second list contain the values of key'''

'''list1=["a","b","c","d","e","f","g","h"]
list2=["1","2","3","4","5","6","7","8"]
dictionary=dict(zip(list1,list2))
print(dictionary)'''
#OR
'''s1="ashirbad"
s2="zxcvbnnm"
dictionary=dict(zip(s1,s2))
print(dictionary)'''
'''Q) GIVEN A STRING AND A NUMBER N WE NEED TO MIRROR THE CHRATER FROM THE NTH POSITION
UP TO LENGTH OF STRING IN ALPHABETICAL ORDER.IN MIRROR OPERATION,WE CHANGE "a" TO "z"
,"b" AND SO ON'''
'''input_string=input("enter the string:")
n=int(input("enter n:"))
#creating dictionary for mirror operation
alphabates="abcdefghijklmnopqrstuvwxyz"
reverse_alphabates=alphabates[::-1]
dict1=dict(zip(alphabates,reverse_alphabates))
#finding the part of string on which we will do mirror operation
prefix=input_string[0:n-1]
suffix=input_string[n-1:]
#finding the mirror string
mirror=""
for i in range(0,len(suffix)):
    mirror=mirror+dict1[suffix[i]]
    #creating the final string
    res=prefix+mirror
    mirror(res)'''



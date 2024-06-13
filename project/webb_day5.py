'''dict={
    "ash":1234,
    "naruto":169,
    "goku":17345,
    "luffy":21324

}
print(dict)
print(type(dict))
print(len(dict))
#accesing element from dictionary
print(dict["ash"])
print(dict.get("naruto"))
dict_1={
    "zoro":1234566789
}
dict.update(dict_1)
print(dict)
#changing the vlue of a key
dict["ash"]=4321
print(dict)
dict.pop("zoro")
print(dict)
dict.popitem()
print(dict)
#print all keys of a dict
for x in dict:
    print(x)
for x in dict.items():#give all the key with it value
    print(x)  
for x,y in dict.items():
    print(x,y)
for x in dict:
    print(dict[x])'''

#nested dictionary
'''area={
    "area_1":{
        "a":12,
        "b":13,
        "c":14 
          },
    "area_2":{
        "x":1,
        "y":2,
        "z":3

    }    

} 
print(area["area_1"]["a"]) 
print(area["area_2"]["y"])'''
sum=0
'''input={
    "a":100,
    "b":200,
    "c":300

} 
for x in input:
    print(input[x])
    sum=sum+input[x]  

print(sum)'''

input_1={
    "x":25,
        "y":18,
            "z":45
}
for i in input_1:
    sum=sum+input_1[i]

print(sum)
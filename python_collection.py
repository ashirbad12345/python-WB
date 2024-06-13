#LIST
#print a list
#list=["banana","orange","mango","papaya"]
# print("your list is",list)
#print("the data type of list is",type(list))
#print("length of the given list is:",len(list))
#CHECKING AN ITEM PRESENT IN THE LIST
'''if "grapes" in list:
    print("grapes is present in the list")
else:
    print("grapes is not present in the list") '''

#ACCESSING ITEM IN THE LIST
#USING INDEXING 
'''print("give the item at index",list[2])
#USING RANGE INDEXING
print(list[0:4])
#USING NEGATIVE INDEXING
print(list[-2])
#USING NEGATIVE INDEXING
print(list[-3:-1])'''


#ADDING ELEMENT TO A LIST
 #1.USINING INSERT(INDEX:ITEM)
'''list.insert(3,"grapes")
print(list)
#using append(elment)=it add the element in the last index of list
list.append("kiwi")
print(list)
#using extend(another list)
list1=["guava","pineapple"] 
list.extend(list1)
print(list)'''

#REMOVING ELMENT FROM LIST
'''list.remove("papaya")
print(list)
list.pop(2)
print(list)'''

#changing item in a list
'''list[1]="cherry"
print(list)
#list[1:3]="papaya"
list[2]=["cocumber"]
print(list)'''

#SORTING OF ELEMENT OF A LIST
'''list.sort()
print(list)#arrange the elem-ent of list in accending order
list.sort(reverse=True)
print(list)'''
'''n=int(input("enter the size of the list"))
list=[]
for i in range (n):
    num=int(input())
    list.append(num)
    print(list)
idx1=int(input("enter the 1st indexing"))
idx2=int(input("enter the second number"))
temp=list[2]
list[idx1]=list[idx2]
list[idx2]=temp
print("after swapping")
print(list)'''


#TUPLE IN PYTHON
tuple=("lilly","lotus","dalia","sunflower")
print(tuple)
print(tuple)








       
 



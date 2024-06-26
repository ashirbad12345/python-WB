class Complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def showNumber(self):
     print(self.real,"i +",self.image,"j")

def add(self,num2):
    newReal=self.real + num2.real
    newImage=self.img +num2.img  
    return Complex(newReal,newImage)    


num1 =Complex(1,3)    
num1.showNumber()   

num2= Complex(4,6)
num2.showNumber()

num3= num1.add(num1)
num3.showNumber()
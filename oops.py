'''class Example:
    name="Ashirbad"
    age="19"
    dist="Balasore"
    ph_no=8458015796

ash=Example()
print(ash.name,ash.age,ash.dist,ash.ph_no)'''

'''class Student:
    def set_name(self,name):
        self.name=name
    def get_name(self):
        return self.name
student1=Student()

student1.set_name("ashirbad") 
print(student1.get_name()) '''

class Rectangle:
    def set_dimension(self,height,width):
        self.height=height
        self.width=width
    def area(self):
        return self.height*self.width
    def perimeter(self):
        return 2*(self.height*self.width)
rectangle1=Rectangle()
h=int(input("enter the height:"))
w=int(input("enter the width:"))
rectangle1.set_dimension(h,w)
print("the height and width are:",rectangle1.height,rectangle1.width)
print("area is:",rectangle1.area())
print("perimeter is:",rectangle1.perimeter())

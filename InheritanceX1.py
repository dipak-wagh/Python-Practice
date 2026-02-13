class Parent:
    def __init__(self):
        self.No1 = 10
        self.No2 = 20
    
    def greet(self):
        print("Inside Parents greet method:",self.No1,self.No2)
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.A = 2
        self.B = 5
    
    def gun(self):
        print("Inside child's gun method",self.A,self.B)

cobj = Child()
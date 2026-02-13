class A:
    def feature1(self):
        print("Feature 1 is working")

    def feature2(self):
        print("Feature2 is working")

class B(A):
    def feature3(self):
        print()

a1= A()
a1.feature1()
a1.feature2()
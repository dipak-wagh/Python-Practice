Addition = lambda No1,No2: (No1 + No2)
Subtraction = lambda No1,No2: (No1 - No2)


No1 = 0
No2 = 0
Ans = 0

No1 = int(input("Enter first number: "))
No2 = int(input("Enter second number: "))

Ans = Addition(No1,No2)
print("Addition is: ",Ans)

Ans = Subtraction(No1,No2)
print("Subtraction is: ",Ans)

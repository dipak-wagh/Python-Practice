number = int(input("Enter the number:"))  # 153
num=number # num=153
digit,sum=0,0 # digit=0, sum=0
length=len(str(num)) # length=3
for i in range(length):  # 0 to 2 # 0,1,2
    digit=int(num%10)   # 3 5 1
    num=num/10          # 15 1 0
    sum=sum+pow(digit,length)# (0+3^3=27) (27+5^3 125=152) (152+1^3=153)
if sum == number:
    print("Armstrong")
else:
    print("Not Armstrong")
# num=int(input("Enter the number:"))
# temp=num
# reverse=0
# while temp > 0:
#     remainder=temp%10
#     reverse=(reverse*10)+remainder
#     temp=temp//10

# if num==reverse:
#     print('palindrome')
# else:
#     print("Not Palindrome")

num = int(input("Enter the number:"))
temp=num
reverse=0
while temp>0:
    remainder=num%10
    reverse=(reverse*10)+remainder
    temp=temp//10

if num==reverse:
    print("Palindrome")
else:
    print("Not PAlindrome")

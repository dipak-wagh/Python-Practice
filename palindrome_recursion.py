def recurrev(number,rev):# (121,0) (12,1) (1,12) (0,121)
    if number == 0:
        return rev
    
    remainder = int(number%10) # 1 2 1
    rev = (rev*10)+remainder   # 1 12 121
    return recurrev(int(number/10),rev) # (12,1) (1,12) (0,121)

num=int(input("Enter the number:")) #121
reverse=0
reverse=recurrev(num,reverse)

print(str(num) + " is :",end="")
print("Palindrome") if reverse == num else print("Not palindrome")
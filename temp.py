def recurfun(number,reverse):
    if number==0:
        return reverse
    remainder = int(number%10)
    reverse = (reverse*10)+remainder
    return recurfun(int(number/10),reverse)

number=input("Enter the number:")
reverse=0
result = recurfun(number,reverse)
print("Reverse no is:",result)

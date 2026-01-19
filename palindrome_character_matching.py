def checkPalindrome(str):
    for i in range(0,len(str)):
        if str[i] != str[len(str) - i - 1]:
            return False
    return True

s="kayak"
print("Palindrome") if checkPalindrome(s) else print("Not Palindrome")


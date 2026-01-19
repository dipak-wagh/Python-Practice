def checkPalindrome(str):
    reverse = ''.join(reversed(str))

    if str == reverse:
        return True
    
    return False

# main function
s="kayak"

print("Palindrome") if checkPalindrome(s) else print("not palindrome")
n = input()
rev = ''
for char in n:
    rev = char + rev
if n==rev:
    print("Palindrome")
else:
    print("Not Palindrome")
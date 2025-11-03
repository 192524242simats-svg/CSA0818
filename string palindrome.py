string=input("Enter a string:")
string=string.lower()
reverse_string=string[::-1]
if string==reverse_string:
    print("The given string is a palindrome")
else:
    print("The given string is not a palindrome")

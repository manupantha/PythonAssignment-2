def is_palindrome(str):
    return str == str[::-1]


str = input("enter the string : ")
result = is_palindrome(str)
if result:
    print(True)
else:
    print(False)

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("racecar"))  
print(is_palindrome("hello"))    
print(is_palindrome("level")) 
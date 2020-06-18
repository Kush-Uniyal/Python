def is_palindrome(name):
    reverse_name= name[::-1]
    if reverse_name==name:
        return True
    else:
        return False
print(is_palindrome("math"))
        

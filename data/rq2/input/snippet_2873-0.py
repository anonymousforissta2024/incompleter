def is_palindrome(s):
    if len(s) < 1:
        return True
    elif s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False
if is_palindrome(a) == True:
    print('String is a palindrome!')
else:
    print("String isn't a palindrome!")
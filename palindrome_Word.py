def is_palindrome(nc_string):
    string = nc_string.casefold()
    return string[::-1] == string


input_string = input("Please enter a word to check, if it is palindrome or not! ")

if is_palindrome(input_string):
    print("'{}' is a palindrome".format(input_string))
else:
    print("'{}' is not a palindrome".format(input_string))
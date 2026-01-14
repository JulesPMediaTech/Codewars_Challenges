# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

def create_phone_number(n):
    s = list(map(str, n))
    return f'({"".join(s[0:3])}) {"".join(s[3:6])}-{"".join(s[6:10])}'

def create_phone_number2(n):
    s = ''.join(map(str, n))
    return f'({s[0:3]}) {s[3:6]}-{s[6:10]}'

def create_phone_number3(n):
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

    
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
arr = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0]
print (f'''\n phone number: {create_phone_number3(arr)}
       ''')

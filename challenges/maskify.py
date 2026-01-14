# return masked string. 
# All characters replaced with a '#' except for the last 4
def maskify(cc):
    return ''.join(map(lambda x: '#', cc[:-4])) + cc[-4:] 

def maskify2(cc):
    return '#' * (len(cc)-4) + cc[-4:]
    

string = "1234 5678 9012 dd3Z56rr"
print (f'''\nMasked input is:
{maskify(string)}\n''')

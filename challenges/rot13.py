'''
Docstring for rot13
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after it in the alphabet. 
ROT13 is an example of the Caesar cipher.
Create a function that takes a string and returns the string ciphered with Rot13. 
If there are numbers or special characters included in the string, they should be returned as they are. 
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".
Please note that using encode is considered cheating.

------

How can you tell an extrovert from an introvert at NSA?
Va gur ryringbef, gur rkgebireg ybbxf ng gur BGURE thl'f fubrf.

I found this joke on USENET, but the punchline is scrambled. Maybe you can decipher it?
According to Wikipedia, ROT13 is frequently used to obfuscate jokes on USENET.

For this task you're only supposed to substitute characters. Not spaces, punctuation, numbers, etc.

Test examples:
"EBG13 rknzcyr." -> "ROT13 example."
"This is my first ROT13 excercise!" -> "Guvf vf zl svefg EBG13 rkprepvfr!"

'''



def rot13(message):
    coded = ''
    for m in message:
        if m.isupper(): b = 65
        elif m.islower(): b = 97
        else: b = 0
        coded = coded + chr ((ord(m)-b+ 13) % 26 +b) if b!= 0 else coded + m
    return coded
        
def rot13_alt(message):
    PAIRS = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"))
    return "".join(PAIRS.get(c,c) for c in message)            
            
    
    
print (f'a is {ord("a")}')
print (f'z is {ord("z")}')
print (f'A is {ord("A")}')
print (f'Z is {ord("Z")}')



example = 'This is my first ROT13 excercise!'
example2 = 'Guvf vf zl svefg EBG13 rkprepvfr!'
print (rot13_alt(example2))


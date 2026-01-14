def is_pangram(st):
    ''' A Pangram is a sentence that uses every letter of the alphabet at least once '''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lettercount = []
    for letter in st.lower():
        if letter not in alphabet:
            continue
        if letter not in lettercount:
            lettercount.append(letter)
    
    return all (letter in lettercount for letter in alphabet)   # replaces the # 4 lines below
        
    # for letter in alphabet:
    #     if letter not in lettercount:
    #         return False
    # return True


print (f' Pangram is {is_pangram("The quick brown fox jumps over the lazy dog")}')


def _kai_is_pangram(st):
    st = st.lower()
    return all(map(lambda x: x in st,'qwertyuiopasdfghjklzxcvbnm' ))

def kai2_is_pangram(st):
    st = set(st.lower())
    for i in st:
        if i.isalpha():
            string += i
            
    return 'abcdefghijklmnopqrstuvwxyz' == "".join(i for i in sorted(string))



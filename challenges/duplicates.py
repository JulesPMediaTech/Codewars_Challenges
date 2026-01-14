def duplicate_count(text):
    # Your code goes here
    letcount,dup  = {}, 0
    for t in text.lower():
        letcount[t] = letcount[t] + 1 if t in letcount else 1
    dup = len([i for i in letcount.values() if i > 1])
    return dup
     
def duplicate_count2(s):
  return len([c for c in set(s.lower()) if s.lower().count(c)>1])

     
print (f'''\n
number of duplicates: {duplicate_count('indivisibility')}\n''')
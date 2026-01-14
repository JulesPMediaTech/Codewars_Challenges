"""
You probably know the "like" system from Facebook and other pages. 
People can "like" blog posts, pictures or other items. 
We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. 
It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""

def likes(names):
    n = len(names)
    match n: 
        case 0: return "no one likes this"
        case 1: return f"{names[0]} likes this"
        case 2: return "{} and {} like this".format(*names)
        case 3: return "{}, {} and {} like this".format(*names)
        # case n if n > 3: return "{}, {} and {others} others like this".format(*names,others=n-2)
        case _: return "{}, {} and {others} others like this".format(*names,others=n-2)
        # case n if n > 3: return f'{names[0]}, {names[1]} and {n-2} others like this'

def likes2(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


names = ['Peter', 'John', 'Paul', 'steve', 'phil']    
# names = ['a','b']    
print (likes(names))
        


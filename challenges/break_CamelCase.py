"""
Docstring for Dev.CodeWars_challenges.break_CamelCase

Complete the solution so that the function will break up camel casing, using a space between words.
Examples:
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  ""

"""
def solution(s):
    for i in s:
        if i.isupper() and s[s.index(i)-1] != ' ':
            s = s.replace(i, f' {i}')
    return s

# def solution2(s):
#     return ''.join(' ' + c if c.isupper() else c for c in s)

# import re
# def solution3(s):
#     return re.sub('([A-Z])', r' \1', s)

text = "camel CasingDeltoid"
print(f'''\n fixed camel case: {solution(text)}
''')
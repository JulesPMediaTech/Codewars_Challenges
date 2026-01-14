def high_and_low(numbers):
    # takes a string of numbers and returns a string with highest number _space_ loweest number
    ints = sorted([ int(i) for i in numbers.split(' ') ])
    return f'{ints[-1]} {ints[0]}'


def high_and_low2(numbers):
    # ...
    ints = sorted(numbers.split(),key=int)
    return f'{ints[-1]} {ints[0]}'


nums = ("1 2 -3 4 5")
print (f'''\nhigh low string result: {high_and_low2(nums)}
''')
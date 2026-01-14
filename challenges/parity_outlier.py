def find_outlier(integers):
    is_even = [i % 2 == 0 for i in integers ]
    return integers[is_even.index(False)] if is_even.count(True) > 1 else integers[is_even.index(True)]




# arr = [2, 4, 0, 100, 4, 11, 2602, 36]
arr = [160, 3, 1719, 19, 11, 13, -21]
print (f'''\nin this array of otherwise all odd or even numbers:
{arr}
the outlier is: {find_outlier(arr)}\n''')

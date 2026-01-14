def square_digits(num):
    # Your code here
    squares = [int(i)**2 for i in (str(num))]
    return int(''.join(str(s) for s in squares))


print (f'result: {square_digits(745)}')

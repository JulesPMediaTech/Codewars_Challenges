def fibonacci (st,le):
    seq = st
    for _ in range(le - 2):
        seq.append(seq[-1] + seq[-2])
    return seq

def tribonacci(signature, n):
    seq = signature
    for _ in range(n - 3):
        seq.append(seq[-1] + seq[-2] + seq[-3])
    return seq[:n]

start, length = [0,1], 20

print (f'''\nfibonacci starting from {start} and a sequence length of {length} numbers:
{fibonacci(start,length)}\n''')

start, length = [1,1,1], 0
print (f'''\ntribonacci starting from {start} and a sequence length of {length} numbers:
{tribonacci(start,length)}\n''')

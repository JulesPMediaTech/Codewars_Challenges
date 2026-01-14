'''
A format for expressing an ordered list of integers is to use
a comma separated list of either individual integers or a range of integers 
denoted by the starting integer separated from the end integer in the range by a dash, '-'. 
The range includes all integers in the interval including both endpoints. 
It is not considered a range unless it spans at least 3 numbers. For example "12,13,15-17"
Complete the solution so that it takes a list of integers in increasing order 
and returns a correctly formatted string in the range format.

solution([-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20])
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"
'''
def solution(args):
    st, r = '', [0]
    for n in args[1:] + [None]:
        if n == r[-1]+1:
            r.append(n)
        else:
            if len(r) > 2:
                st += f'{r[0]}-{r[-1]},'
            elif len (r) == 2:
                st += f'{r[0]},{r[1]},'
            else:
                st += f'{r[0]},'
            r = [n]
    return st[2:-1]

def solution2(arr):
    ranges = []
    a = b = arr[0]
    for n in arr[1:] + [None]:
        if n != b+1:
            ranges.append(str(a) if a == b else "{}{}{}".format(a, "," if a+1 == b else "-", b))
            a = n
        b = n
    return ",".join(ranges)
            
            
            
        

        
    
ordered = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]

print (solution2 (ordered))
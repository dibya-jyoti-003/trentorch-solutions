def summation(f, lo, hi):
    sum = 0 
    for i in range (lo, hi+1):
        sum += f(i)
    return sum

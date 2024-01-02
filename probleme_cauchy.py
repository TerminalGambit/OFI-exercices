# cn = cn-1 + cn-2 - cn-3
# c0 = 0, c1 = 1, c2 = 1

def cauchy(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0:
        result = 0
    elif n == 1:
        result = 1
    elif n == 2:
        result = 1
    else:
        result = cauchy(n-1, memo) + cauchy(n-2, memo) - cauchy(n-3, memo)
    
    memo[n] = result
    return result

print(cauchy(50), cauchy(73))

# cn = cn-1 + cn-2 - cn-3
# c0 = 0, c1 = 1, c2 = 1

def cauchy(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return cauchy(n-1) + cauchy(n-2) - cauchy(n-3)

print(cauchy(50), cauchy(73))
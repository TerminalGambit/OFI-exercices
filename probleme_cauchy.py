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

# cn = cn-2 + n
# c1 = 1, c0 = 0

def cauchy2(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = cauchy2(n-2, memo) + n
    
    memo[n] = result
    return result

print(cauchy2(50), cauchy2(73))

# cn = cn-1 + n
# c0 = 0

def cauchy3(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0:
        result = 0
    else:
        result = cauchy3(n-1, memo) + n
    
    memo[n] = result
    return result

# solution générale est p(n) où p est un polynôme de degré 2 ? vrai ou faux ?
# p(n) = an² + bn + c
# pourquoi ? car p(n) = p(n-1) + n
# p(n-1) = a(n-1)² + b(n-1) + c
# p(n) = a(n-1)² + b(n-1) + c + n

# cn = 2ncn-1 + 1
# c0 = 0

def cauchy4(n, memo={}):
    if n in memo:
        return memo[n]
    elif n == 0:
        result = 0
    else:
        result = 2*n*cauchy4(n-1, memo) + 1
    
    memo[n] = result
    return result

def test_solution(f):
    for n in range(10):
        print(f(n))

def cas_n(n):
    return 2**n * factorial(n) + (-1)**n

def cas_n2(n):
    return 2**n + (-1)**(n)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print("Test cas_n:")
test_solution(cas_n)
print("\nTest cas_n2:")
test_solution(cas_n2)
print("\nTest cauchy4:")
test_solution(cauchy4)
def find_fibonacci_iter(n):
    f0 = 0
    f1 = 1
    if type(n) != int:
        raise TypeError(f"Input argument should be of type 'int' while it was of type '{type(n)}'")
    if n < 0:
        raise Exception("Input argument should be greater than or equal to 0")
    if n == 0:
        return f0
    if n == 1:
        return f1
    for i in range(2, n+1):
        current_fib = f0 + f1
        f0 = f1
        f1 = current_fib
    return current_fib

# making recursive fibonacci function more efficient using memoization
fibonacci_cache = {0: 0, 1: 1}
def find_fibonacci_recur(n):
    if type(n) != int:
        raise TypeError(f"Input argument should be of type integer but instead was of type {type(n)}")
    if n < 0:
        raise ValueError("Input argument should be a natural number")
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    else:
        value = find_fibonacci_recur(n-2) + find_fibonacci_recur(n-1)
    fibonacci_cache[n] = value
    return value

# 100: 354224848179261915075
for i in range(11):
    print(f"{i}: {find_fibonacci_recur(i)}")

print(find_fibonacci_recur(3.3))
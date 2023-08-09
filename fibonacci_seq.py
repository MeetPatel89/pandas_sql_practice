def find_fibonacci_iter(n):
    f0 = 0
    f1 = 1
    for i in range(n+1):
        if i == 0:
            print(f0)
        if i == 1:
            print(f1)
        if i > 1:
            current_fib = f0 + f1
            print(current_fib)
            f0 = f1
            f1 = current_fib

find_fibonacci_iter(8)
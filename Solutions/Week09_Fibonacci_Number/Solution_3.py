def fib(n):
    fibonacci = [1, 2]
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci[n-1] if n > 1 else 1

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    n = int(input())
print(fib(n))
def fib(n):
    num1 = 1
    num2 = 2
    for i in range(2, n):
        num1, num2 = num2, num1 + num2
    return num2 if n > 1 else num1

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    n = int(input())
    print(fib(n))
def reverse(L):
    # your code here

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    L = eval(input())
    rL = reverse(L)
    print(L)
    print(rL)
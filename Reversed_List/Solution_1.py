def reverse(L):
    if not isinstance(L, list): return L.reverse()
    return [reverse(x) for x in reversed(L)]

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    L = eval(input())
    rL = reverse(L)
    print(L)
    print(rL)
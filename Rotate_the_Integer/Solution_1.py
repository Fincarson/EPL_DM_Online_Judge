T = int(input())

for t in range(T):
    x = int(input())
    if(x >= 128): print(f"Case #{t+1}: {((x-128) << 1) +1}")
    else: print(f"Case #{t+1}: {x << 1}")
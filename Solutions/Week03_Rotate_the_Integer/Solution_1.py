for T in range(int(input())):
    x = int(input())
    if(x >= 128): print(f"Case #{T+1}: {((x-128) << 1) +1}")
    else: print(f"Case #{T+1}: {x << 1}")
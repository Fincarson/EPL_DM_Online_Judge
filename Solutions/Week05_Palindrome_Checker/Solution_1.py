for T in range(int(input())):
    L = input().split()
    if(L == L[::-1]): print(f"Case #{T+1}: Yes")
    else: print(f"Case #{T+1}: No")
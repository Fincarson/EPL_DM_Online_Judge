for T in range(int(input())):
    L = input().split()
    print(f"Case #{T+1}: Yes" if L == L[::-1] else f"Case #{T+1}: No")
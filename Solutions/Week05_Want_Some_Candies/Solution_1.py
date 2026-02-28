for T in range(int(input())):
    n = list(map(int, input().split()))
    print(f"Case #{T+1}: {min(len(set(n)), len(n) // 2)}")
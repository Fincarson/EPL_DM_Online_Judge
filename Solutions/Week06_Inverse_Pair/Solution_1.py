for T in range(int(input())):
    L = list(map(int, input().split()))
    n = len(L)
    output = 0

    for i in range(n):
        for j in range(i+1, n):
            if L[i] > L[j]: output += 1
    print(f"Case #{T+1}: {output}")
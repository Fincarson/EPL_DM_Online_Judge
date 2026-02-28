for T in range(int(input())):
    L = list(map(int, input().split()))
    for i in reversed(range(len(L))):
        L[i] += 1
        if(L[i] < 10): break
        L[i] = 0
    if L[0] == 0: L = [1] + L
    print(f"Case #{T+1}: {L}")
for T in range(int(input())):
    L = list(map(int, input().split()))
    for i in reversed(range(len(L) - 1)):
        L[i] += 1
        if(L[i] < 10): break
    if L[0] == 0: L = [1] + L
    print(f"Case #{T+1}: {L}")
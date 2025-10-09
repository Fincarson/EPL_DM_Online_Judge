for T in range(int(input())):
    n = list(map(int, input().split()))
    n = sorted(n)
    output = -1
    for i in range(len(n)):
        if(i != n[i]):
            output = i
            break

    if output == -1: output = len(n)
    print(f"Case #{T+1}: {output}")
for T in range(int(input())):
    t = int(input())
    L = list(map(int, input().split()))

    hashmap = {}
    for i in range(len(L)):
        num = L[i]
        if t-num in hashmap:
            print(f"Case #{T+1}: {[hashmap[t-num], i]}")
            break
        hashmap[num] = i
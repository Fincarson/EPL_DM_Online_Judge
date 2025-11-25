def possible_number(output, binary, startIndex, n, k):
    if(k == 0):
        num = 0
        for i in range(n): num += binary[i] * (1 << i)
        return output + [num]

    for i in range(startIndex, n):
        binary[i] = 1
        output = possible_number(output, binary, i + 1, n, k - 1)
        binary[i] = 0
        
    return output

for T in range(int(input())):
    n, k = map(int, input().split())
    print(f"Case #{T+1}: {sorted(possible_number([], [0]* n, 0, n, k))}")
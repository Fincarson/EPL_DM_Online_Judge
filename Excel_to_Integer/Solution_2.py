for T in range(int(input())):
    c = input()
    result = 0
    for i in range(len(c)):
        result = result * 26
        result += ord(c[i]) - 64
    print(f"Case #{T+1}: {result}")
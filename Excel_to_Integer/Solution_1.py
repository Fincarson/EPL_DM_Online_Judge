for T in range(int(input())):
    c = input()
    num = 0
    output = 0
    for ch in (c[::-1]):
        num *= 26
        output += (ord(ch) - 64) * (num if num != 0 else 1)
        num += 1 if num == 0 else 0
    print(f"Case #{T+1}: {output}")
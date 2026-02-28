for T in range(int(input())):
    num = int(input())
    output = ""
    while num > 0:
        num -= 1
        output += chr(num%26 + 65)
        num //= 26
    print(f"Case #{T+1}: {output[::-1]}")
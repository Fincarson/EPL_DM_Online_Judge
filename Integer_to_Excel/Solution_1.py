for T in range(int(input())):
    num = int(input())
    output = ""
    while(num > 26):
        output += chr(num%26 + 64)
        num //= 26
    output += chr(num + 64)
    print(f"Case #{T+1}: {output[::-1]}")

a = ord('a')
A = ord('A')

for T in range(int(input())):
    output = []
    for ch in input():
        if 'a' <= ch <= 'z': output.append(chr((ord(ch) - a + 1) % 26 + a))
        elif 'A' <= ch <= 'Z': output.append(chr((ord(ch) - A + 1) % 26 + A))
        else: output.append(ch)
    print(f"Case #{T+1}: {''.join(output)}")
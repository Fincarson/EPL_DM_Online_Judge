T = int(input())

a = ord('a')
A = ord('A')

for t in range(T):
    output = []
    for ch in input():
        if 'a' <= ch <= 'z': output.append(chr((ord(ch) - a + 1) % 26 + a))
        elif 'A' <= ch <= 'Z': output.append(chr((ord(ch) - A + 1) % 26 + A))
        else: output.append(ch)
    print(f"Case #{t+1}: {''.join(output)}")
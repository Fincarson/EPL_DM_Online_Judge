for T in range(int(input())):
    text = input().split()
    print(f"Case #{T+1}: {text[0].find(text[1])}")
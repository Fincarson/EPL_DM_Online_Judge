for T in range(int(input())):
    text = input()
    n = int(input()) 
    if text != "": n = n % len(text)
    print(f"Case #{T+1}: {text[n:] + text[:n]}")
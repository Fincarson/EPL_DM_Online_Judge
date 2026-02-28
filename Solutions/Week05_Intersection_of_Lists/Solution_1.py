for T in range(int(input())):
    num1 = list(map(int, input().split()))
    num2 = list(map(int, input().split()))
    print(f"Case #{T+1}: {sorted(list(set(num1) & set(num2)))}")
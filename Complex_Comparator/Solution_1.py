for T in range(int(input())):
    num = input().split()
    num[0] += "+0j" if num[0].find('j') == -1 else ""
    num[1] += "+0j" if num[1].find('j') == -1 else ""
    
    a, b = list(map(int, num[0].replace('j', '').split('+')))
    c, d = list(map(int, num[1].replace('j', '').split('+')))
    
    op = ''
    if(a > c and b > d): op = '>'
    elif(a < c and b < d): op = '<'
    elif(a == c and b == d): op = '=='
    elif(a >= c and b >= d): op = '>='
    elif(a <= c and b <= d): op = '<='
    else: op = '!='
    
    num[0] = num[0][2:] if num[0][0] == '0' else "(" + num[0] + ")"
    num[1] = num[0][2:] if num[1][0] == '0' else "(" + num[1] + ")"
    print(f"Case #{T+1}: {num[0]} {op} {num[1]}")
tcase = int(input())

for t in range(tcase):
    s = input()
    r = int(input())

    if(r == 0): #no rotation
        print(f"Case #{t + 1}: {s}")
        continue

    rotate = r % len(s)
    if (rotate<0):
        rotated = rotate + len(s)
    
    rotated_string = s[rotate:] + s[:rotate]

    print(f"Case #{t + 1}: {rotated_string}")

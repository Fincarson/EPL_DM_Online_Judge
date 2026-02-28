def pascal(row, col):
    return 1 if (col == 0 or row == col) else (pascal(row-1, col-1) + pascal(row-1, col))

def print_pascal(n):
    for i in range(n):
        print(''.join(f'{pascal(i, j):3d}' for j in range(i + 1)))

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    n = int(input())
    print_pascal(n)
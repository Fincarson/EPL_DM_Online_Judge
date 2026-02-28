class Matrix:
    def __init__(self, size, m):
        self.size = size
        self.m = m

    def __add__(self, rhs):
        return Matrix(self.size, [[self.m[i][j] + rhs.m[i][j] for j in range(self.size)] for i in range (self.size)])

    def __sub__(self, rhs):
        return Matrix(self.size, [[self.m[i][j] - rhs.m[i][j] for j in range(self.size)] for i in range(self.size)])

    def __mul__(self, rhs):
        return Matrix(self.size, [[sum(self.m[i][k] * rhs.m[k][j] for k in range(self.size)) for j in range(self.size)] for i in range(self.size)])

    def __repr__(self):
        return '\n'.join([' '.join(map(str, self.m[i])) for i in range(self.size)])

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    k = int(input())
    m1_list = []
    for _ in range(k):
        m1_list.append(list(map(int, input().split())))

    m2_list = []
    for _ in range(k):
        m2_list.append(list(map(int, input().split())))

    m1 = Matrix(k, m1_list)
    m2 = Matrix(k, m2_list)
    print(m1+m2)
    print(m1-m2)
    print(m1*m2)
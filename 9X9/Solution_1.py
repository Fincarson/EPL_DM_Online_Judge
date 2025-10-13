def get_products(a=1, b=9, c=1, d=9):
    output = []
    for i in range(a, b+1):
        for j in range(c, d+1):
            output.append(i*j)
    return output
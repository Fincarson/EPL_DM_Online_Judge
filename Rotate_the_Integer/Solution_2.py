tcase = int(input())

for i in range (tcase) :
    num = int(input())

    rotated_num = ((num << 1) & 0xFF) | ((num >> 7) & 0x01)

    print(f"Case #{i+1}: {rotated_num}")
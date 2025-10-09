roman_dictionary = {
    1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
    100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
    10: 'X', 9: 'IX', 5: 'V', 4: 'IV',
    1: 'I'
}

for T in range(int(input())):
    num = int(input())
    output = ""
    for i in (roman_dictionary.keys()):
        while(num >= i):
            output += roman_dictionary[i]
            num -= i
    print(f"Case #{T+1}: {output}")

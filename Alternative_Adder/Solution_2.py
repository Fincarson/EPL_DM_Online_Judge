def adder(*args):
    output = 0
    for i in (args[0::2]): output += i
    for i in (args[1::2]): output -= i
    return output

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        args = map(int, input().split())
        print("Case #%d: %d" % (i, adder(*args)))
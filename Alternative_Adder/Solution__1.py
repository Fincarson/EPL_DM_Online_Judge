def adder(*args):
    output = 0
    for i in range(len(args)):
        if(i & 1): output -= args[i]
        else: output += args[i]
    return output

if __name__ == '__main__':
    t = int(input())
    for i in range(1, t+1):
        args = map(int, input().split())
        print("Case #%d: %d" % (i, adder(*args)))
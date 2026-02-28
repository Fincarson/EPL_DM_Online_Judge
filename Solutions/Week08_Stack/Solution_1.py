stack = []
qSum = 0
def init():
    global stack, qSum
    stack = []
    qSum = 0
    return None

def push(val):
    global stack, qSum
    stack.append(val)
    qSum += val * val
    return None

def pop():
    global stack, qSum
    val = stack.pop()
    qSum -= val * val
    return None

def top():
    global stack, qSum
    return stack[-1]

def getSquareSum():
    global stack, qSum
    return qSum
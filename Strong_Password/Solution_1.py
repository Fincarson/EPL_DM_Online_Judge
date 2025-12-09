from re import search

def is_strong(passwd):
    if len(passwd) < 8: return False
    if not search(r'[a-z]', passwd): return False
    if not search(r'[A-Z]', passwd): return False
    if not search(r'\d', passwd): return False
    if not search(r'[-!@#$%^&*()+]', passwd): return False
    for a, b in zip(passwd, passwd[1:]):
        if a == b: return False

    return True


# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    passwd = input()
    if is_strong(passwd):
        print('Strong')
    else:
        print('Weak')
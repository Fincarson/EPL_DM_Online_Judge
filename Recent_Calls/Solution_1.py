class RecentCounter:

    def __init__(self):
        self.list = []

    def ping(self, t):
        self.list.append(t)
        num = 0
        tmin = t - 3000
        for x in self.list: num += 1 if(x in range(tmin, t+1)) else 0
        return num

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(1,T+1):
    counter = RecentCounter()
    calls = list(map(int,input().split()))
    for ind,time in enumerate(calls):
        print(f'Case #{t}_{ind}: {counter.ping(time)}')
def permute(nums):
    # your code here

# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    nums = list(map(int, input().split()))
    print(permute(nums))
def permute(nums):
    if len(nums) == 0: return []
    if len(nums) == 1: return [nums]

    result = []
    for i in range(len(nums)):
        tmp = permute(nums[i+1:] + nums[:i])
        for t in tmp: result.append([nums[i]] + t)
    return result


# Note that the following code is for local testing purposes only. You should leave this part of code unchanged and not submit it to the OJ system.
T = int(input())
for t in range(T):
    nums = list(map(int, input().split()))
    print(permute(nums))
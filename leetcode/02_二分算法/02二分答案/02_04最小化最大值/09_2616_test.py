from typing import List

nums = [1,1,2,3,7,10]
p = 2
def check(mx: int) -> bool:
    cnt = i = 0
    while i < len(nums) - 1:
        if nums[i + 1] - nums[i] <= mx:
            cnt += 1
            i += 2
        else:
            i += 1
    return cnt >= p

print(check(4))
# https://leetcode.com/problems/product-of-array-except-self/description/
def solution(nums):
    res = [1] * len(nums)
    for i in range(1, len(nums)):
        res[i] = nums[i-1] * res[i-1]
    suffix = 1
    for i in range(len(nums)-1, -1, -1):
        res[i] = res[i] * suffix
        suffix = nums[i] * suffix
    return res

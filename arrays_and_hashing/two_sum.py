# https://leetcode.com/problems/two-sum/description/
def solution(nums, target):
    temp_dict = {}
    for i, num in enumerate(nums):
        diff = target-num
        if diff in temp_dict:
            return [temp_dict[diff], i]
        temp_dict[num] = i
    return [0, 0]

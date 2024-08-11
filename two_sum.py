# https://leetcode.com/problems/two-sum/description/
def solution(nums, target):
    temp_dict = {}
    for i in range(len(nums)):
        diff = target-nums[i]
        if diff in temp_dict.keys():
            return [temp_dict.get(diff), i]
        temp_dict[nums[i]] = i
    return [0, 0]

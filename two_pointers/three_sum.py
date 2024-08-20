# https://leetcode.com/problems/3sum/description/
def solution(nums):
    nums.sort()
    res = []
    for i, n in enumerate(nums):
        l_index = i + 1
        r_index = len(nums) - 1
        if i > 0 and n != nums[i-1]:
            while l_index < r_index:
                ans = n + nums[l_index] + nums[r_index]
                if ans > 0:
                    r_index -= 1
                elif ans < 0:
                    l_index += 1
                else:
                    res.append([n, nums[l_index], nums[r_index]])
                    l_index += 1
                    r_index -= 1
                    while l_index < r_index and nums[l_index] == nums[l_index-1]:
                        l_index += 1
    return res




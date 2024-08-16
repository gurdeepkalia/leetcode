# https://leetcode.com/problems/longest-consecutive-sequence/description/
def solution(nums):
    nums_set = set(nums)
    longest = 0
    for n in nums:
        if n-1 not in nums_set:
            count = 0
            while (n+count) in nums_set:
                count += 1
            longest = max(longest, count)
    return longest


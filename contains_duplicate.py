# https://leetcode.com/problems/contains-duplicate/
def solution(nums):
    hashset = set()
    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

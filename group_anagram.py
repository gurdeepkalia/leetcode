# https://leetcode.com/problems/group-anagrams/description/
from collections import defaultdict


def solution(strs):
    res = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    return res.values()

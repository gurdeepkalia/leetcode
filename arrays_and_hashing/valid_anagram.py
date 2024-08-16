# https://leetcode.com/problems/valid-anagram/
'''
dict(a=1, b=2) == dict(a=2, b=1)
False

dict(a=1, b=2) == dict(a=1, b=2, c=0)
False

dict(a=1, b=2) == dict(b=2, a=1)
True
'''


def solution(s: str, t: str):
    if len(s) != len(t):
        return False
    count_s, count_t = {}, {}
    for i in range(len(s)):
        count_s[s[i]] = 1 + count_s.get(s[i], 0)
        count_t[t[i]] = 1 + count_t.get(t[i], 0)
    return count_s == count_t

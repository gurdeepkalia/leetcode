# https://leetcode.com/problems/valid-palindrome/description/
"""
# solution1
def solution(s: str):
    alphanum_str = ""
    for c in s:
        if c.isalnum():
            alphanum_str += c.lower()
    return alphanum_str == alphanum_str[::-1]
"""


# solution2
def solution(s: str):
    l, r = 0, len(s)-1
    while l < r:
        while l < r and not is_alpha_num(s[l]):
            l += 1
        while l < r and not is_alpha_num(s[r]):
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


def is_alpha_num(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))

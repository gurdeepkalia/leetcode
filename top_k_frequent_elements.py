# https://leetcode.com/problems/top-k-frequent-elements/description/
def solution(nums, k):
    count = {}
    freq_list = [[] for i in range(len(nums) + 1)]
    res = []
    for n in nums:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq_list[c].append(n)
    for i in range(len(nums), 0, -1):
        for n in freq_list[i]:
            res.append(n)
            if len(res) == k:
                return res


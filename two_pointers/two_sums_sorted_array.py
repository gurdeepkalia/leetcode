def solution(numbers, target):
    l_index = 0
    r_index = len(numbers) - 1
    while l_index < r_index:
        if numbers[l_index] + numbers[r_index] < target:
            l_index += 1
        elif numbers[l_index] + numbers[r_index] > target:
            r_index -= 1
        else:
            return [l_index + 1, r_index + 1]
    return [0, 0]


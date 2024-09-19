# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from arrays_and_hashing import (contains_duplicate,
                                longest_consecutive_seq,
                                valid_anagram,
                                two_sum,
                                group_anagram,
                                top_k_frequent_elements,
                                product_of_array_except_self,
                                valid_sudoku)
from two_pointers import (valid_palindrome,
                          two_sums_sorted_array,
                          three_sum,
                          container_with_most_water,
                          trapping_rain_water)
from stack import (valid_parentheses, minstack)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(contains_duplicate.solution([1, 2, 3, 1]))
    # print(valid_anagram.solution("anagram", "nagaram"))
    # print(two_sum.solution([2, 7, 11, 15], 26))
    # print(group_anagram.solution(["eat", "tea", "tan", "ate", "nat", "bat"]))
    # print(top_k_frequent_elements.solution([1, 1, 1, 2, 2, 3], 2))
    # print(product_of_array_except_self.solution([1, 2, 3, 4]))
    """print(valid_sudoku.solution([["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                , [".", "6", ".", ".", ".", ".", "1", "8", "."]
                                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    """
    # print(longest_consecutive_seq.solution([100, 200, 4, 1, 3, 2]))
    # print(valid_palindrome.solution("A man, a plan, a canal: Panama"))
    # print(two_sums_sorted_array.solution([-1, 0], -1))
    # print(three_sum.solution([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    # print(container_with_most_water.solution([1, 8, 6, 2, 5, 4, 8, 3, 7]))
    # print(trapping_rain_water.solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    # print(valid_parentheses.solution("()[]{}"))
    min_stack = minstack.MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(3)
    print(min_stack.get_min())  # return -2
    min_stack.pop()
    print(min_stack.top())  # return 0
    print(min_stack.get_min())  # return -2





# duplicate integer
# https://neetcode.io/problems/duplicate-integer

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dictionary = {}
        for num in nums:
            if num not in dictionary.keys():
                dictionary[num] = 1
            else:
                return True
        else:
            return False
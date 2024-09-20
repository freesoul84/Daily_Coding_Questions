# majority elements
# https://leetcode.com/problems/majority-element/

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary = {}
        if len(nums)>2:
            for i in nums:
                if i not in dictionary:
                    dictionary[i] = 1
                else:
                    dictionary[i] += 1
                    if dictionary[i] > len(nums)//2:
                        return i
        else:
            return nums[0]
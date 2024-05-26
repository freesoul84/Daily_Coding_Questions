# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums):

        ans = 0 
        for i in list(set(nums)):
            if nums.count(i)>(len(nums)/2):
                return i       
            
obj = Solution()
print(obj.majorityElement([1,1,1,1,3,4]))
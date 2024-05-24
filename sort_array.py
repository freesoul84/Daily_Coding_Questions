# https://leetcode.com/problems/sort-an-array/description/
class Solution:
    def sortArray(self, nums):
        i = 0
        j = 0
        while j < len(nums): 
            for i in range(0, len(nums)-j-1):
                if nums[i] > nums[i+1]:
                    nums[i],nums[i+1] = nums[i+1], nums[i]
            j += 1
        return nums


obj = Solution()
print(obj.sortArray([1,3,-2,11,123133,11]))

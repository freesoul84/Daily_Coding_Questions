class Solution:
    def findDisappearedNumbers(self, nums):
        return set(range(1,len(nums)+1)) - set(nums)

obj = Solution()
print(obj.findDisappearedNumbers([1,1,2,3,4]))
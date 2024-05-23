# https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums):

        product = 1
        
        for num in nums:
            product *= num
        
        if product > 0:
            return 1
        elif product < 0:
            return -1
        else:
            return 0
        
obj = Solution()
print(obj.arraySign([-1,1,1,1,2,3,4,-1]))
print(obj.arraySign([-1,1,1,1,2,3,4,1]))
print(obj.arraySign([-1,1,1,1,2,3,4,0]))

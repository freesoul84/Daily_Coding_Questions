# https://leetcode.com/problems/range-sum-query-immutable/
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right) :
        res = 0
        for i in self.nums[left:right + 1]:
            res += i
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

a = NumArray([1,2,3,4,5,6])
print(a.sumRange(0,3))
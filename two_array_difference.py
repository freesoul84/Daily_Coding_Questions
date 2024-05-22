# https://leetcode.com/problems/find-the-difference-of-two-arrays/

class Solution:
    def findDifference(self, nums1, nums2):
        ans = list()
        ans.append([])
        for i in nums1:
            if i not in nums2 and i not in ans[0]:
                    ans[0].append(i)
        ans.append([])
        for i in nums2:
            if i not in nums1 and i not in ans[1]:
                    ans[1].append(i)
        return ans

a = Solution()
print(a.findDifference([1,2,3,4],[-111,11,1]))
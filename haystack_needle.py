# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

# Code approach:
"""
We need to find the first occurance of the pattern. to iterate over the matching needle we need to subtract that length from haystack then only we can iterate over it.
"""
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        length = len(haystack) - len(needle)
        for i in range(0,length + 1):
            if haystack[i:len(needle)+i] == needle:
                return i
        else:
            return -1

obj = Solution()
print(obj.strStr(haystack="abcdefghijklmno", needle="lmno"))
            
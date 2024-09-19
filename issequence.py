# issequence
# https://leetcode.com/problems/is-subsequence/submissions/1395331523/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j = 0,0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
        if len(s) == i:
            return True
        else:
            return False
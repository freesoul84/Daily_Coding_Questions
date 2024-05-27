# https://leetcode.com/problems/isomorphic-strings/
class Solution:
    def isIsomorphic(self, s, t):
        if len(set(s)) != len(set(t)):
            return False
        else:
            map = {}
            for i in range(len(s)):
                if s[i] not in map:
                    map[s[i]] = t[i]
                elif  s[i] in map:
                    if map[s[i]] == t[i]:
                        continue
            
            st = ''.join([map[i] for i in s])
            if st == t:
                return True
            else:
                return False

obj = Solution()
print(obj.isIsomorphic("egg","add"))
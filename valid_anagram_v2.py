# valid anagram
# https://leetcode.com/problems/valid-anagram/description/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            dictionary = {}
            for i in s:
                if i not in dictionary.keys() : 
                    dictionary[i] = 0
                else:
                    dictionary[i] += 1

            for i in t:
                if i not in dictionary or dictionary[i] < 0:
                    return False
                else:
                    dictionary[i] -= 1
            else:
                return True
        else:
            return False
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])

obj = Solution()
print(obj.lengthOfLastWord("ALKESHA RAVINDRA BAIKAR"))
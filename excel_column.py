class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []
        while columnNumber:
            columnNumber, reminder = divmod(columnNumber-1, 26)
            result.append(chr(65 + reminder))
        return ''.join(reversed(result))
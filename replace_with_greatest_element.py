# Replace element with the max element
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        for i in range(len(arr)):
            if i != len(arr)-1:
                arr[i] = max(arr[i+1:])
            else:
                arr[i] = -1
        return arr
    

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        rightmax = -1
        for i in range(len(arr)-1,-1,-1):
            newmax = max(rightmax,arr[i])
            arr[i] = rightmax
            rightmax = newmax
        return arr

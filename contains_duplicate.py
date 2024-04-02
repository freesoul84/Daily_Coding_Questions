# https://leetcode.com/problems/contains-duplicate/description/

def containsDuplicate(nums) -> bool:
        di = {}
        for i in nums:
            if i not in di.keys():
                di[i] = 1
            else:
                return True
        else:
            return False
        

array = list(map(int, input("Enter array : ").split(",")))
print(containsDuplicate(array))
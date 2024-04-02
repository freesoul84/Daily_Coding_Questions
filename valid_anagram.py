# https://leetcode.com/problems/valid-anagram/description/


def isAnagram(s: str, t: str) -> bool:
    di1 = {}

    for i in s:
        if i not in di1.keys():
            di1[i] = 1
        else:
            di1[i] += 1

    for i in t:
        if i in di1.keys():
            di1[i] -= 1
        else:
            return False

    if len(s) == len(t):
        for i in t:
            if di1.get(i,1) != 0:
                return False
        else:
            return True
    else:
        return False
    
s = input("Enter first string :")
t = input("Enter second string :")
print(isAnagram(s,t))
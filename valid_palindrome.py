# ascii of number 0 to  9 is : 48 to 57.
# ascii of character a to z is : 97 to 122
# leetcode problem : https://leetcode.com/problems/valid-palindrome/

# solution 1
def isPalindrome(s: str) -> bool:
    s = s.lower()
    new_str = ''.join([i for i in s if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)])
    print(new_str)
    reverse_str = new_str[::-1]
    if new_str == reverse_str:
        return True
    else:
        return False

print(isPalindrome("a b c c b a"))
        
# solution 2

def isPalindrome_2(s: str) -> bool:
    s = s.lower()
    print(s)
    new_str = ''.join([i for i in s if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=48 and ord(i)<=57)])
    for i in range(len(new_str)//2):
        if new_str[i] == new_str[len(new_str)-i-1]:
            continue
        else:
            return False
    else:
        return True

print(isPalindrome_2("a b c c b a"))
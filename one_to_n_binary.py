# Code to return n number of binary numbers start from 1 to n
# there is a pattern. For every second and third number it is nothing but appends of first number with suffix 0 and 1 respectively.
# 1 10 11 100 101 110 111 1010 1011 1100 1101

n = int(input("Enter number of binary numbers you require : "))

from collections import deque
queue = deque()
queue.append("1")

for i in range(0,n):
    ele = queue.popleft()
    queue.append(ele + "0")
    queue.append(ele + "1")
    print(ele, end = " ")

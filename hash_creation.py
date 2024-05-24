# https://leetcode.com/problems/design-hashmap/submissions/1266256023/

class MyHashMap:

    def __init__(self):
        self.hashmap = {}

    def put(self, key: int, value: int) :
        self.hashmap[key] = value

    def get(self, key: int):
        if key in self.hashmap.keys():
            return self.hashmap[key]
        else:
            return -1

    def remove(self, key: int):
        if key in self.hashmap.keys():
            del self.hashmap[key]


#Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
key = 1 
value = 11
print(obj.put(key,value))
key = 1
param_2 = obj.get(key)
print(param_2)
key = 1
obj.remove(key)
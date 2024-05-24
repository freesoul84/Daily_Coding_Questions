# https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        self.hashset = []

    def add(self, key: int) -> None:
        if key not in self.hashset:
            self.hashset.append(key)

    def remove(self, key: int) -> None:
        if key in self.hashset:
            del self.hashset[self.hashset.index(key)]

    def contains(self, key: int) -> bool:
        if key in self.hashset:
            return True
        else:
            return False


# Your MyHashSet object will be instantiated and called as such:
obj = MyHashSet()
key = 11
obj.add(key)
key = 12
obj.add(key)
key = 11
obj.remove(key)
key = 12
param_3 = obj.contains(key)
print(param_3)



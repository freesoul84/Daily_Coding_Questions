# https://leetcode.com/problems/design-parking-system/

class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        di = {1:[0]*big,2:[0]*medium,3:[0]*small}
        val = {1: 0, 2:0, 3:0}    
        self.di = di
        self.val = val

    def addCar(self, carType: int) -> bool:
        if self.val[carType] < len(self.di[carType]):
            self.val[carType] += 1
            return True
        else:
            return False 

obj = ParkingSystem(big = 1, medium = 2, small=3)
param_1 = obj.addCar(1)
print(param_1)
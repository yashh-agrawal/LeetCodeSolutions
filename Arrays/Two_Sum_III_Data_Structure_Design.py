# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.

# Implement the TwoSum class:

# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.

class TwoSum:

    def __init__(self):
        self.arr = []
        

    def add(self, number: int) -> None:
        self.arr.append(number)

    def find(self, value: int) -> bool:
        result = False
        if self.arr is None:
            return result
        left = 0
        right = len(self.arr) - 1
        self.arr.sort()
        while left < right:
            total = self.arr[left] + self.arr[right]
            if total == value:
                return True
            elif total > value:
                right -= 1
            else:
                left +=1 
        return result


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)
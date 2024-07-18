# Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        count = 0
        for i in range(len(arr)):
            if arr[i] % 2 != 0:
                count += 1
            elif arr[i] % 2 == 0 and count < 3:              
                count = 0    
        return count >= 3
# Given an array arr, replace every element in that array with the greatest element among the elements to its right, 
# and replace the last element with -1.
# After doing so, return the array.

class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        maxi = -1
        for i in range(n-1,-1,-1):
            temp = arr[i]
            arr[i] = maxi
            maxi = max(maxi,temp)
        return arr
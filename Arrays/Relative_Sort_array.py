# Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

# Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
# Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        output = []

        for i in arr2:
            while i in arr1:
                output.append(i)
                arr1.remove(i)
        return(output+sorted(arr1))
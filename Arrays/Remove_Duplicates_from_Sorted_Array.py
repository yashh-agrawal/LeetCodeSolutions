# Solution 1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=1
        j = nums[0]

        for i in range(len(nums)):
            if nums[i] != j:
                nums[k] = nums[i]
                j = nums[i]
                k+=1
        return k

# Solution 2

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i == 0 or nums[i]!=nums[i-1]:
                nums[k]=nums[i]
                k+=1
        return k     
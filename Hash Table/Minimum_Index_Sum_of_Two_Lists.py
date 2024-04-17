# Given two arrays of strings list1 and list2, find the common strings with the least index sum.

# A common string is a string that appeared in both list1 and list2.

# A common string with the least index sum is a common string such that if it appeared at list1[i] and list2[j] 
# then i + j should be the minimum value among all the other common strings.

# Return all the common strings with the least index sum. Return the answer in any order.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_val = -1
        res = {}
        arr = []
        for i, l1 in enumerate(list1):
            for j, l2 in enumerate(list2):
                if l1==l2:
                    res[l1] = i+j
                    if min_val == -1:
                        min_val = i + j
                    else:
                        min_val = min(min_val, i + j)
        for k,v in res.items():
            if v == min_val:
                arr.append(k)
        return arr
        
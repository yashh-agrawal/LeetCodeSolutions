# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = Counter(nums)
        ans = fre_counter.most_common()
        arr = []
        for key, _ in ans:
            if k<=0:
                break
            k -=1
            arr.append(key) 
        return arr
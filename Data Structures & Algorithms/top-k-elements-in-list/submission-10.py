class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[]for i in range(len(nums) + 1)]

        for i in nums:
            count[i] = count.get(i, 0) + 1
        for c,n in count.items():
            freq[n].append(c)
        
        res = []
        for i in range(len(freq) -1, -1, -1):
            for j in freq[i]:
                res.append(j)
            if len(res) == k:
                return res
        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = [[] for i in range(len(nums) + 1)]
        count = {}
        for i in nums:
            count[i] = count.get(i, 0) + 1
        for i, j in count.items():
            x[j].append(i)
        
        res = []
        for i in range(len(x) -1, -1, -1):
            for j in x[i]:
                res.append(j)
            if len(res) == k:
                return res

        
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_map = {}
        count = [[]for i in range(len(nums) + 1)]

        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1
        for n, c in hash_map.items():
            count[c].append(n)
        
        res = []
        for i in range(len(count) -1, 0, -1):
            for n in count[i]:
                res.append(n)
                if len(res) == k:
                    return res

        
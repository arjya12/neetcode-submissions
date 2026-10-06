class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #diff = 7 - 3 = 4
        #diff = 7 - 4 = 3
        # 4 = 7 - 3
        hash_map = {}

        for i,j in enumerate(nums):
            diff = target - j
            if diff in hash_map:
                return [hash_map[diff], i]
            hash_map[j] = i


        
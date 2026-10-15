class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_map = {}
        longest = 0
        x = set(nums)

        for i in nums:
            if (i - 1) not in x:
                length = 0
                while (i + length) in x:
                    length += 1
                longest = max(length, longest)
        return longest
        
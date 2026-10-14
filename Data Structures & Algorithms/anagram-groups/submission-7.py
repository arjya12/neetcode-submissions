class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for i in strs:
            x = [0] * 26
            for j in i:
                x[ord(j) - ord("a")] += 1
            hash_map[tuple(x)].append(i)
        return list(hash_map.values())
        
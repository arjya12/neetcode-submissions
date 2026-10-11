class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for i in strs:
            a = [0] * 26

            for j in i:
                a[ord(j) - ord("a")] += 1
            hash_map[tuple(a)].append(i)
                
        return list(hash_map.values())
        
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_index_map = defaultdict(list)
        for index, string in enumerate(strs):
            anagram_index_map[str(sorted(string))].append(string)
        return list(anagram_index_map.values())
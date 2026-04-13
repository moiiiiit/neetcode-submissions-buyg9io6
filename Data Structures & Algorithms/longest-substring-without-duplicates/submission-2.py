class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        start_idx=0
        end_idx=0
        longest_substring_length=0
        char_hash = {}
        while end_idx<len(s):
            if s[end_idx] in char_hash:
                longest_substring_length = max(longest_substring_length, end_idx-start_idx)
                while s[start_idx] != s[end_idx]:   
                    start_idx += 1
                start_idx += 1
                end_idx = start_idx
                char_hash = {}
            else:
                char_hash[s[end_idx]] = 1
                end_idx += 1
        longest_substring_length = max(longest_substring_length, end_idx-start_idx)
        return longest_substring_length
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_word = min(strs)
        wl = len(min_word)
        for i in range(wl):
            for s in strs:
                if min_word[i] != s[i]:
                    return s[0:i]
        return min_word
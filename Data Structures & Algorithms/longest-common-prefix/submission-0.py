class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        min_word = min(strs)
        wl = len(min_word)
        for i in range(wl):
            for s in strs:
                if min_word[i] != s[i]:
                    return res
            res += min_word[i]
        return res 
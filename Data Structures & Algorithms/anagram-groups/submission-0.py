class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for s in strs:
            freq = [0]*26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            freq = str(freq)
            if freq in hashMap:
                hashMap[freq].append(s)
            else:
                hashMap[freq] = [s]
        return [hashMap[arr] for arr in hashMap]
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, n in enumerate(nums):
            nextNum = target - n
            if nextNum in hashMap and hashMap[nextNum] != i:
                return [hashMap[nextNum], i]
            if n not in hashMap:
                hashMap[n] = i
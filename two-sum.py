from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        if not nums:
            return [] # or return empty list

        for i, num in enumerate(nums):
            if target - num in dic:
                return [i, dic[target - num]]
            dic[num] = i
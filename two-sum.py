from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        if not nums:
            return []  # or return empty list

        for i, num in enumerate(nums):
            if target - num in dic:
                return [i, dic[target - num]]
            dic[num] = i


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    res = Solution().twoSum(nums, 9)
    print(res)

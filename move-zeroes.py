class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        for j in range(i, len(nums)):
            nums[j] = 0

    def moveZeroesV1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        no_zeroes = [num for num in nums if num != 0]
        no_zeroes.extend(0 for _ in range(len(nums) - len(no_zeroes)))
        for i in range(len(nums)):
            nums[i] = no_zeroes[i]

    def moveZeroesV2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = right = 0
        while right < len(nums):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1
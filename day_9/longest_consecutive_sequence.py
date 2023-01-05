class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums.sort()
        nums_len = len(nums)
        i = 1
        count = 1
        longest_count = 1
        while i <= nums_len - 1:
            if nums[i-1] != nums[i]:
                if nums[i] == nums[i-1] + 1:
                    count += 1
                else:
                    longest_count = max(longest_count, count)
                    count = 1
            i += 1
        return max(longest_count, count)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i, j in enumerate(nums):
            rem = target - j
            if rem not in hash_table:
                hash_table[j] = i
            else:
                return [hash_table[rem], i]

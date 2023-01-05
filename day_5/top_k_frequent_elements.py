class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        i = 0
        res = []
        hash_map = {}
        while i < len(nums):
            val = nums[i]
            if val in hash_map:
                hash_map[val] += 1
            else:
                hash_map[val] = 1
            i += 1
        k_elem = sorted(hash_map.items(), key=lambda item: item[1])[len(hash_map)-k:]
        for i in k_elem:
            res.append(i[0])
        return res

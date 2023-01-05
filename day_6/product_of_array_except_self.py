class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        backward_cum_arr = []
        result = []
        N = len(nums) - 1
        prev = 1
        while N > 0:
            prev = prev * nums[N]
            backward_cum_arr.insert(0, prev)
            N -= 1
        forward_cum = nums[0]

        result.append(backward_cum_arr[0])

        for i in range(1, len(backward_cum_arr)):
            curr = forward_cum * backward_cum_arr[i]
            result.append(curr)
            forward_cum *= nums[i]
        result.append(forward_cum)
        return result



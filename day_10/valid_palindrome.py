class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_str = [i for i in s if i.isalnum()]
        l = 0
        r = len(clean_str) - 1
        while l <= r:
            if clean_str[l].casefold() != clean_str[r].casefold():
                return False
            l += 1
            r -= 1
        return True
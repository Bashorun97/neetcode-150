class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return True if s == t else False
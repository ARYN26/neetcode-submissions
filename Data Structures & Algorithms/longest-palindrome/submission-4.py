class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = sum(v // 2 * 2 for v in Counter(s).values())
        return 1 + length if length < len(s) else length
     
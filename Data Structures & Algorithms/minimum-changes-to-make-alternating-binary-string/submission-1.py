class Solution:
    def minOperations(self, s: str) -> int:
        count = sum(1 for i, c in enumerate(s) if int(c) == i % 2)
        return min(count, len(s) - count)
class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        max_odd = max(v for v in c.values() if v%2==1)
        min_even = min(v for v in c.values() if v%2==0)

        return max_odd - min_even
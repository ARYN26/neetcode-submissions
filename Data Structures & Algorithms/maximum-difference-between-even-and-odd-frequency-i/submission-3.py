class Solution:
    def maxDifference(self, s: str) -> int:
        c = Counter(s)

        odd = max(v for v in c.values() if v%2==1)
        even = min(v for v in c.values() if v%2==0)

        return odd - even
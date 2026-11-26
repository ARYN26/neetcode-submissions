class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = defaultdict(int)
        countS[chr] += 1

        return Counter(s) == Counter(t)
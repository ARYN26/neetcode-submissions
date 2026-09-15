class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max([n for n, c in Counter(arr).items() if n == c], default=-1)


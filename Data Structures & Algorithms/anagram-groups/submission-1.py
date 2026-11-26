class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in strs:
            if "".join(sorted(i)) in d:
                d["".join(sorted(i))].append(i)
            else:
                d["".join(sorted(i))] = [i]
        return list(d.values())


## Complexity
#- Time: $O(n x klogk)$
#- Space: $O(n x k)$

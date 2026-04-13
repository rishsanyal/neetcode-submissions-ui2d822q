class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # We could sort all of them and use a dict

        res = defaultdict(list)

        for i in strs:
            temp_i = ''.join(sorted(i))

            res[temp_i].append(i)

        return res.values()
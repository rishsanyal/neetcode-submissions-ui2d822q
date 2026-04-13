class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # check the dict len

        s_dict, t_dict = defaultdict(int), defaultdict(int)

        for i in s:
            s_dict[i] += 1

        for j in t:
            t_dict[j] += 1

        for k, v in s_dict.items():
            if k not in t_dict or v != t_dict[k]:
                return False

            t_dict.pop(k)

        return len(t_dict) == 0

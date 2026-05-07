class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        we need to track who's trusted by whom.

        if any trustees = n-1 the trusted key is the winner.

        We can use a dict for this (defaultdict(list))
        as we iterate through, if at any point we're at n-1, we've found the winner
        """

        d = defaultdict(set)
        res = -1

        maybe_res = set()
        invalid_res = set()

        for a,b in trust:
            d[b].add(a)

            if len(d[b]) == n-1:
                maybe_res.add(b)


        for maybe_judge in maybe_res:
            for key, val in d.items():
                if key == maybe_judge:
                    continue

                if maybe_judge in val:
                    invalid_res.add(maybe_judge)
                    break

        result = maybe_res - invalid_res

        return result.pop() if result else -1
                
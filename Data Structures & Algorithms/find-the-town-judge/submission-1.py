class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        """
        we need to track who's trusted by whom.

        if any trustees = n-1 the trusted key is the winner.

        We can use a dict for this (defaultdict(list))
        as we iterate through, if at any point we're at n-1, we've found the winner
        """

        incoming_trust = defaultdict(set)
        outgoing_trust = defaultdict(set)

        for a,b in trust:
            incoming_trust[b].add(a)
            outgoing_trust[a].add(b)


        for i in range(n):
            if len(incoming_trust[i]) == n-1 and not outgoing_trust[i]:
                return i

        return -1
                
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        """
        Union Find is better because it's more space efficient and we don't have to iterate through the account multiple times
        parent - (name, index)
        Rank - number of emails for that parent - in a dict
        Track (parent, index) by name of accounts - in a dict

        edges -
            {
                "neet@gmail.com": [2,0,3]
            }

        parent - 
            {
                idx: idx
            }
            
        rank -
            {
                0, 3,
                2: 3,
                3: 1
            }

        All of the accounts WILL have the same name

        create graph
        def find -> for every email that has 2 parents

        def union(idx1, idx2)


        for email, parents in parent.items():
            while len(parents) >= 2:
                n1, n2 = parents.pop(0), parents.pop(0)
                parent[email].append(parent[n1])

        # Format and return
        """

        edges = defaultdict(set)
        rank = defaultdict(int)
        parent = [i for i in range(len(accounts))]

        res = []

        for idx, account_info in enumerate(accounts):
            name, emails = account_info[0], account_info[1:]

            for email in emails:
                edges[email].add(idx)
            
            rank[idx]=len(account_info)

        def find(email_idx):
            if email_idx != parent[email_idx]:
                parent[email_idx] = find(parent[email_idx])

            return parent[email_idx]

        def union(idx1, idx2):
            if idx1 == idx2:
                return

            r1, r2 = rank[idx1], rank[idx2]

            if r1 >= r2:
                parent[idx2] = idx1
                rank[idx1] += rank[idx2]
            else:
                parent[idx1] = idx2
                rank[idx2] += rank[idx1]

            return


        for edge_idx, vertices in edges.items():
            while len(vertices) >= 2:
                n1, n2 = vertices.pop(), vertices.pop()
                p1, p2 = find(n1), find(n2)

                union(p1, p2)

                vertices.add(find(p1))

            # Not sure if this is necessary
            edges[edge_idx] = vertices
        
        # print(parent)

        result = {}

        for idx, val in enumerate(parent):
            root = find(idx)
            val = root
            #get name from val idx
            if val not in result:
                result[val] = {
                    "name": accounts[idx][0],
                    "emails": set(accounts[idx][1:]),
                }
            else:
                result[val]["emails"] |= set(accounts[idx][1:])

        for _, val in result.items():
            res.append([val['name']] + list(val['emails']))

        return res


        


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        """
        We need a directed graph with a value.

        When can an answer not be determined?
            Two numbers aren't connected
            there's a cycle


        equations = [["a","b"],["b","c"],["ab","bc"]], 
        values = [4.0,1.0,3.25], 
        queries = [["a","c"],["b","a"],["c","c"],["ab","a"],["d","d"]]

        Output: [4.00000,0.25000,1.00000,-1.00000,-1.00000]


        {
            "a" : 
                {
                    "b": 4
                },
            "b":
                {
                    "a": 1/4,
                    "c": 1
                },
            "c":
                {
                    "b": 1
                },
            "ab":
                {
                    "bc": 3.25
                },
            "bc":
                {
                    "ab": 1/3.25
                }
        }

        we need to keep multiplying at every stage
        we need to track the current number
        we need to track the parent and the number we're looking for
        parent, curr_num=1, target_number:
            for child in graph[curr_num]:
                if child == parent:
                    continue

                if child != target_number:
                    if ans := dfs(child, graph[parent][child]*curr_num, target_number):
                        return ans
                else:
                    return graph[parent][child]*curr_num

            return -1
        """

        graph = defaultdict(lambda: defaultdict(int))
        res = []

        for idx, (i,j) in enumerate(equations):
            graph[i][j] = values[idx]
            graph[j][i] = 1/values[idx]

        def dfs(curr_node, target_num, curr_num, visited):
            if curr_node in visited:
                return None

            if target_num in graph[curr_node]:
                return curr_num*graph[curr_node][target_num]

            visited.add(curr_node)

            for child in graph[curr_node]:
                if child in visited:
                    continue
                
                ans = dfs(child, target_num, graph[curr_node][child]*curr_num, visited)
                if ans:
                    return ans

            return None

        for (i,j) in queries:
            if (i not in graph) or (j not in graph):
                res.append(-1)
                continue

            if i == j:
                res.append(1)
                continue

            if num := dfs(i, j, 1, set()):
                res.append(num)
            else:
                res.append(-1)

        return res
















            
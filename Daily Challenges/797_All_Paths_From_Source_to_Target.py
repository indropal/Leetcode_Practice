class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.graph = collections.defaultdict(list)

        for i, edges in enumerate(graph):
            self.graph[i] = edges

        res = []

        def dfs(currPath, currNode):
            if currNode == len(self.graph) - 1:
                res.append(list(currPath)[:])

            for connection in self.graph[currNode]:
                currPath.append(connection)
                dfs(currPath, connection)
                currPath.pop()

        dfs([0], 0)

        return res

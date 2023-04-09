class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        
        N = len(colors) # get the number of nodes in graph
        ans = -1
        # for nodes which are terminal nodes in graph & not in edge list, include an empty list
        adj = { n : [] for n in range(N) } 

        # construct adjacency list
        for n1, n2 in edges:
            if not adj.get(n1):
                adj[n1] = []
            adj[n1].append(n2)

        # run depth first search starting from every node in the graph while maintaing a track of the 
        # visited node & path of traversal - we do not want to traverse the same node more than once.
        # We can keep track of the largest color-value for each possible path starting a given node & 
        # re-use it when the node is an adjacent neighbor of another source node.
        #
        # Hence we do not have to re-traverse a given path.
        # We maintain a freq. matrix for each color in the given graph which gives us the universal
        # color-value of each node of each color.

        # visited ~ set of nodes which have already been visited
        # path ~ set of nodes which are a part of the current path
        visited, path = set(), set()
        
        # maintain a color value matrix ~ Initialize it
        # each color is represesented by lower-case letter of alphabet i.e. 26 distinct values
        # we maintain such freq. map for each node in graph
        colorValueMat = [[0 for _ in range(26)] for n in range(N)] # 'a' is index 0, 'b' is index 1 ...

        def dfs(node):

            if node in path:
                # terminate search as there is a definite cycle in the graph for the current path
                return float("inf")
            
            if node in visited:
                # we want to visit a node ONLY once through our entire search as we are storing 
                # color-count per node per color ~ retraversing is wastage
                return 0
            
            # update visited & path
            visited.add(node)
            path.add(node)

            # obtain the color value for current node & respective index in colorValue matrix
            colorIdx = ord(colors[node])-ord('a')
            colorValueMat[node][colorIdx] = 1 # update color value for existing node for node's color

            # iterate through all the adjacent nodes & update the current-node's adj matrix
            for neiNode in adj[node]:
                # all path & visited get updated per dfs call --> we don't have to handle it here
                if dfs(neiNode) == float("inf"):
                    # there is a loop
                    return float("inf")
                
                # update color values for all possible colors in path including the adjacent node
                # for the current node
                for c in range(26):
                    colorValueMat[node][c] = max( colorValueMat[node][c],
                                                  (1 if c == colorIdx else 0) + colorValueMat[neiNode][c]
                                                )
            # remove the current node from path as we want to consider other paths & keep track of cycles
            path.remove(node)
            # return the maximum color value for the current node in dfs
            return max(colorValueMat[node])
        

        # run dfs through each node & each dfs implicitly computes the max color value for the node
        for n in range(N):
            tmpVal = dfs(n)

            if tmpVal == float("inf"):
                ans = -1 # there is a cycle
                break
            else:
                ans = max(ans, tmpVal)
        
        return ans
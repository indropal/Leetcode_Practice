class Solution:

    def longestPath(self, parent: List[int], s: str) -> int:
        # Construct adjacency matrix from the parent list
        adjMat = collections.defaultdict(list)

        for i, node in enumerate(parent):
            # if parent[i] == -1:
            #     # -1 isn't actually a node in the tree, its a reference
            #     # for the root node of the tree
            #     continue
            # adjMat[i].append(parent[i])

            # Store parent to Node mapping
            adjMat[node].append(i)
        
        # print(adjMat)
        ans = 1

        # Use DFS to traverse the tree in a manner such that no pair of "adjacent"
        # nodes i.e. parent-child nodes have the same character in them
        #
        # DFS as for longest path, its preferable to have parent-till-leaf node
        # traversal rather than fanning out in each level of the graph / tree
        def dfs(childNode):

            nonlocal ans            
            longestPath, secondLongestPath = 0, 0

            # for each element in the adjacency list of child node - traverse &
            # find the maximum length of the path possible
            for node in adjMat[childNode]:

                # traverse this node path as adjacent nodes do not have same value
                # pathLength += 1
                # check the traversal for the next node
                childPath = dfs(node)
                
                if s[childNode] != s[node]:

                    if longestPath < childPath:
                        secondLongestPath = longestPath
                        longestPath = childPath

                    elif secondLongestPath < childPath:
                        secondLongestPath = childPath
                
            ans = max(ans, longestPath + secondLongestPath + 1)
            
            return longestPath + 1

        dfs(0)

        return ans
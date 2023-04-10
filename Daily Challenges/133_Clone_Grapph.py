"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':

        if not node:
            return node
        
        # create a new copy Node for the current node ~ its the first node in graph
        # we need to create copy of the nodes which are its neighbors via BFS
        srcNode = Node(val=node.val)

        # run DFS on all its neightbors & subsequent neightbors while creating copies
        # maintain a hashset for visited nodes as we do not want to copy the same node multiple times
        # we maintain a map of the visited node which is ampped to its cloned node
        visited = {}; visited.update({node: srcNode})

        def dfs(node, srcNodeRef):

            if not node:
                return
            
            if node in visited:
                # node has already been visited, the neighbor node is a reference to itself
                # just include it in the neighbor list
                srcNodeRef.neighbors.append(visited[node])
                return
            
            copyNode = Node(val=node.val)
            srcNodeRef.neighbors.append(copyNode) # include the copied node into SourceNode's neighbors
            visited.update({node: copyNode}) # current node has now been visited
            
            # run DFS to generate clones of the neighbors for the current copied node
            for neiNode in node.neighbors:
                dfs(neiNode, copyNode)
            
            return
        
        # initiate DFS from the cloned sourceNode
        for neiNode in node.neighbors:
            dfs(neiNode, srcNode)
        
        return srcNode





import sys
from functools import lru_cache

sys.setrecursionlimit(100000) # not necessary

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        """
        # this solution is not the best solution as it makes a lot of recursive calls
        # which can cause the call-stack to overflow.
        #
        # The premise is that for every node which contain an apple, we have to take 2 seconds
        # to traverse to that node and back i.e. traverse to node with apple -> collect apple -> traverse back to its parent
        # thus an overall of 2 seconds.
        # The idea is to use DFS / BFS to get to these nodes with apples & collect them & traverse back to their parent node
        # as we have to make our make back to Vertix 0 position from where we started.
        # Hence for each node with an apple or on the way to a node with apple we'll have 2 seconds for traversal.
        #
        # Why choose DFS ??
        # It is best to explore all children of each node without returning to the root.
        # This will avoid travelling the same path multiple times. Hence we choose Depth first Search.
        # For a parent node if we know the values necessary to process its children / sub-trees, then these values can be used to
        # process its parent node. we can use the answer computed for the children nodes to get the answer for parent node - 
        # for which Depth-First-Search is a good algorithm


        if n == 1:
            return sum([0 < apple for apple in hasApple])

        ans = -1
        # create an adjacency matrix from the list of edge pairs
        adjMat = {}
        for e1, e2 in edges:
            if not adjMat.get(e1):
                adjMat[e1] = []
            if not adjMat.get(e2):
                adjMat[e2] = []
            adjMat[e1].append(e2)
            adjMat[e2].append(e1)
        
        def dfs(x):
            for v in adjMat[x]:
                adjMat[v].remove(x)
                dfs(v)
        dfs(0)

        @lru_cache(None)
        def apple(x):
            if hasApple[x]:
                return True
            
            for v in adjMat[x]:
                if apple(v):
                    return True
            return False
        
        def traverse(x):
            total = 0
            for v in adjMat[x]:
                if apple(v):
                    total += traverse(v) + 2
            return total

        return traverse(0)
        """

        # more streamlined solution
        adjMat = collections.defaultdict(list)
        visited = set() # keep track of nodes visited

        # Create an adjacency matrix from the list of edge-vertice-pairs
        for e1, e2 in edges:
            adjMat[e1].append(e2)
            adjMat[e2].append(e1)
        # print(adjMat, "\n", hasApple)

        # for each subtree of root node p, find the time taken to collect all apples
        # present in the subtree
        # we start with the root node 0, whose parent (for reference - not given in problem) is -1
        # use dfs to calculate the total time taken to collect apples from node's tree
        
        def dfs(node, parentNode):
            # This function recursively computes the time taken to traverse & collect the
            # apples in a child-node's subtree of parent-node.
            # totalTime to collect apples from subtree of parentNode
            # childTime is time to collect apples from all child subtrees of parent node
            totalTime, childTime = 0, 0
            # print("-->>", node, parentNode, childTime, totalTime)

            # iterate through all the nodes in the adjacency list for current visited node
            for childNode in adjMat[node]:
                
                if childNode == parentNode:
                    # the childNode connects with the parentNode - since we have already
                    # visited the parentNode, we do not need to visit it again.
                    # hence continue iterating to other nodes in adjacency list
                    continue

                # function call for the childNode to go through its adjacency list
                # and check the time taken to collect all apples in the child sub-tree
                childTime = dfs(childNode, node)
                
                # if 0 < childTime, there are nodes with apples in this child subtree
                # if the childTime == 0, then there are no apples in the subtree of the childNode
                # hence we won't bother traversing it - hence not adding to totalTime
                # On the flip-side, if the childNode which is the root of the child-subtree has an
                # apple, then we will need to traverse the child node (root-node) of child-sub=tree
                # thereby adding 2 seconds to the time taken for traversal
                if (childTime or hasApple[childNode]):
                    totalTime += childTime + 2

                # print(childNode, parentNode, childTime, totalTime)
                
            return totalTime
            
        return dfs(0, -1)
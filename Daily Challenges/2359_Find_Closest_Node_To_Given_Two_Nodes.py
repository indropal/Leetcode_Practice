class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        # This is Directed graph with atmost one outgoing edge, there could be
        # multiple incoming edges to a single node & also result in cycles
        #
        # ~> iterate through all nodes in the graph from provided node1 & node2
        #    while maintaining a list of nodes visited and get the common nodes
        #    reachable from both of them
        
        # populate nodes that can be visited from node1 & node2 in hashSet
        # visited1 = set() # we dont need this anymore - can get visit info from path arrayy
        # visited2 = set() # we dont need this anymore- can get visit info from path arrayy
        N = len(edges)
        common = [] # cache for common nodes
        node = None
        
        # get the path starting from node1 & node2 respectively ~ 
        # we know that there can be atmost len(edges) num edges
        # numbered [0 <-> n-1], take advantage of this by making the
        # index of path array the node-number & the value store at index 'node' num as
        # the path length
        # if path[node] == -1, then it means that node hasn't been visited
        path1 = [-1 for _ in range(N)]; path1[node1] = 0
        path2 = [-1 for _ in range(N)]; path2[node2] = 0
        pathLen = 0

        # iterate through the directed graph starting from node1
        while True:
            node = edges[node1]
            pathLen += 1

            if node == -1:
                # reached terminal node
                break
            
            # if node already visited then we are starting to cycle -> break the traversal
            # if node in visited1:
            if path1[node] != -1:
                # we are starting to cycle & we dont want to visit again
                break
            
            # update visited, path & continue
            # visited1.add(node)
            # path1.append(node)
            path1[node] = pathLen
            node1 = node # update to next node
        
        pathLen = 0 # re-init
        # check if node2 is in path1 already
        if path1[node2] != -1:
            common.append(node2)

        # iterate through the directed graph starting from node2
        while True:
            node = edges[node2]
            pathLen += 1

            if node == -1:
                # reached terminla
                break
            
            # prevent cycling through multiple times
            # if node in visited2:
            if path2[node] != -1:
                break
            
            # check for common nodes with node1 path
            # if node in visited1:
            if path1[node] != -1:
                common.append(node)
            
            # update the visited path & continue
            # visited2.add(node)
            # path2.append(node)
            path2[node] = pathLen
            node2 = node
        
        #print(path1, path2, common)
        # check for no common nodes at all - if so then return -1
        if not common:
            return -1
        
        # there are common elements & check for their respective pathLens
        # we want the max length possible from either node1 & node2 to the common node
        # to be the minimum one over all common nodes
        minLen = float("inf")
        ans = -1
        for n in common:
            maxPLen = max(path1[n], path2[n])
            
            # There could be multiple common nodes with minimum length ~ pick smallest common node
            # thats why less than equal to comparison for pathLength
            if maxPLen <= minLen:
                # as in Question -> for multiple answers, return one with smallest index
                if maxPLen == minLen:
                    # if the length equal to minlen, then pick smallest index
                    ans = min(ans, n) if ans != -1 else n
                else:
                    ans = n # we got a smaller length, get new node as ans
                
                minLen = maxPLen
            
            #print(n, maxPLen, minLen, ans)
        
        return ans
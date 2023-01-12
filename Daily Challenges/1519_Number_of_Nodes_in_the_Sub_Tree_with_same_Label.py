class Solution:
    def dfs(self, childNode, parentNode, adjMat, labels, hashLabel):

        # Iterate through the adjaccency list of childNode
        # The parent Node will be present in adjacency list as they
        # share an edge - so in that case just skip that node in the
        # traversal loop.
        # we need to keep track of the labels for each node using the
        # HashLabel defined.

        # Increment the initial count with itself
        hashLabel[childNode][ ord(labels[childNode]) - ord('a')  ] += 1
        # hashLabel[childNode][labels[childNode]] = 1

        for node in adjMat[childNode]:

            if node == parentNode:
                # Skip this node as we have already traversed this node
                # go to the next node in the adjacency list
                continue
            
            # get the label frequencies of the child subtree
            # parentNode is now the current 'childNode', while the current 'node' in its adjacency
            # list is its child node. 
            childHashLabel = self.dfs(node, childNode, adjMat, labels, hashLabel)
            
            # print("ParentNode: {} | ChildNode : {}".format(childNode, node), "\n", hashLabel)
            # print("----------------------------")
            
            # update the label hash's frequency ~ copy and update of the respective label frequencies 
            # in its child subtrees
            
            # This was before the hashLabel update
            for labelIdx in range(len(hashLabel[childNode])):
                hashLabel[childNode][labelIdx] += childHashLabel[node][labelIdx]

            # for k, v in childHashLabel[node].items():
            #     if not hashLabel[childNode].get(k):
            #         hashLabel[childNode][k] = 0
            #     hashLabel[childNode][k] += v
            
        return hashLabel

    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        if n == 0:
            return []
        
        # convert the list of pair of nodes i.e. list of edges into adjacency matrix
        adjMat = collections.defaultdict(list)

        # In the Adjacency Matrix the Parent-Child relationship is not exactly established
        # we need to keep that in mind
        for n1, n2 in edges:
            adjMat[n1].append(n2)
            adjMat[n2].append(n1)
        # print("-->>"); print(adjMat); print("-->>")

        # iterate through each node & find the count of the number of nodes with
        # same label in its subtree - use DFS & use the value from the child-tree
        # to obtain the answer for the root-node of sub-tree.
        #
        # Start with the root of tree i.e. node 0
        # We need to keep track of the labels for each node - create a label hash
        # i.e. a LabelHash is where for each node a list of 26 elements exist where
        # each index in the list corresponds to the frequenncy of label respective to
        # 26 letters of the english alphabet.
        #
        # UPDATE : The label Map Hashes mmaybe super sparse ~ we can update the same 
        # with the help of a dictionary which maps label frequencies with label
        # OBS ~ The array approach saves on more memory it seems ..... 
        
        hashLabel = { n : [0]*26 for n in adjMat.keys()}
        # hashLabel = {n : {} for n in adjMat.keys() }
        finalHash = self.dfs(0, -1, adjMat, labels, hashLabel); # print(finalHash)
        
        # Construct the answer from the hashLabel map
        ans = [finalHash[nodeIdx][ord(labels[nodeIdx]) - ord('a')] for nodeIdx in range(n)]; # print(ans)
        # ans = [finalHash[nodeIdx][labels[nodeIdx]] for nodeIdx in range(n)]

        return ans
        

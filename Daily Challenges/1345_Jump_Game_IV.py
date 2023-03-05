class Solution:
    def minJumps(self, arr: List[int]) -> int:
        queue = []
        numSteps = 0
        graph = {}
        N = len(arr)

        if N == 1:
            return numSteps

        # populate the disjoint graph
        for i, ele in enumerate(arr):
            if not graph.get(ele):
                graph[ele] = []    
            graph[ele].append(i)
        
        # print(graph)
        # initialize the queue
        queue.append(0)

        # Use BFS to consider all possibilities & positions in the array
        while queue:
            sizeQ = len(queue)
            numSteps += 1

            for _ in range(sizeQ):
                currPos = queue.pop(0)

                if (currPos == N-1) or (currPos+1 == N-1):
                    return numSteps

                # check for 'currPos-1' position
                if (0 <= currPos-1) and (graph.get(arr[currPos-1])):
                    queue.append(currPos-1)
                
                # check for 'currPos+1' position
                if (currPos+1 < N) and (graph.get(arr[currPos+1])):
                    queue.append(currPos+1)
                
                # consider all entries into the list of positions storing the same array value
                # ~ consider all of them in BFS & then delete the graph key entry as we are already
                # considering all possibilities & don't want to have to redo it again
                if graph.get(arr[currPos]):

                    for ele in graph[arr[currPos]]:
                        if ele != currPos:
                            if ele == N-1:
                                return numSteps
                            queue.append(ele)
                    
                    # remove the currPos key from graph to avoid re-visiting the same positions
                    del graph[arr[currPos]]           

        return -1
        
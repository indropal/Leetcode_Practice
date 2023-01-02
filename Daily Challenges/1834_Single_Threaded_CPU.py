class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        for idx, t in enumerate(tasks):
            # include index in the list of indices
            t.append(idx)

        tasks.sort(key=lambda r: r[0])

        ans, minHeap = [], []
        i, timeElapse = 0, 0

        while minHeap or (i < len(tasks)):
            # iterate through all the tasks which have been sorted by their
            # respective enqueue times
            
            # print(timeElapse, minHeap)

            while (i < len(tasks)) and (tasks[i][0] <= timeElapse):
                # Include the tasks into minHeap whose enqueue times are less than equal to the elapsed time
                # required to process previous tasks ~ Only include the processing time & task index into minHeap
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i += 1

            if not minHeap:
                # the minHeap is empty i.e. there are no current active tasks &
                # the next enququed task in 'tasks' might be very far away
                # So, we directly set the timeElapse to nexxt earliest enqueue task / available
                # task instead of iterating multiple times
                timeElapse = tasks[i][0]
            else:
                # pop the index of the current earliest task to be completed
                # and update the timeElapse
                procTime, taskIdx = heapq.heappop(minHeap)

                # update the elapsed time to process the task
                timeElapse += procTime
                ans.append(taskIdx)

        return ans
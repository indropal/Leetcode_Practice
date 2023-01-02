class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:

        heapPile = []
        originalRocks = sum(piles) # Store total number of rocks initially present

        for p in piles:
            # By default, in Python 'heapq' implementation of heap is in Min-heap format
            # we want the Max heap ~hence negate the values will give us the Max-heap ver. for Min-heap
            heapq.heappush(heapPile, -p)

        for _ in range(k):
            # for each of 'k' operations, deduct half from the pile by taking the max value from pile
            # then deduct half & re-insert into heap.
            # continuously do this for 'k' times & return the sum of remainder rocks in piles

            tmpPile = (-1) * heapq.heappop(heapPile) # negate for original value as it was negated before inserting
            originalRocks -= tmpPile // 2 # subtract from total number of rocks initially present
            tmpPile -= tmpPile // 2

            # reinsert to heap
            heapq.heappush(heapPile, -tmpPile)

        return originalRocks
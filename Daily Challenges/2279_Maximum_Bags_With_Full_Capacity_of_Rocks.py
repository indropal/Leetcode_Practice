class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:

        N = len(capacity)
        i = 0

        # Obtain the residual capacity available per bag to be filled up
        for idx in range(N):
            capacity[idx] -= rocks[idx]

        # sort the residual capacity bags in ascending order so that the bags which require less
        # rocks to reach full capacity get assigned first.
        capacity = sorted(capacity); # print(capacity, N)

        while (i < N) and 0 < additionalRocks:
            additionalRocks -= capacity[i]; #print(additionalRocks)
            if additionalRocks < 0:
                break
            capacity[i] = 0
            i += 1

        return sum([c==0  for c in capacity])
        
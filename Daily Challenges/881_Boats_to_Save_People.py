class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Using a Binary Search Solution
        """
        # sort the weight of people in ascending order
        ans, i = 0, 0
        people.sort()

        # start iterating from the beginning of the list & look for the closest
        # greatest weight / number that is smaller than 'limit - people[i]'
        N = len(people)

        if N == 1:
            ans = 1 if (people[0] <= limit) else 0
            return ans

        left, right = 0, N-1

        def bSearch(l, r, target):
            idx = None
            while l <= r:
                mid = l + (r-l)//2

                if people[mid] <= target:
                    idx = mid
                    l = mid + 1
                else:
                    r = mid - 1
            return idx
        
        while i < N:
            # print(people[i], i, people)

            if 0 < limit-people[i]:
                # there's 
                ansIdx = bSearch(i+1, N-1, limit-people[i])
                
                # If there's someone else appropriate in the array else its just 
                # current person -> people[i]
                if ansIdx:
                    # remove the chosen person from the array
                    people.pop(ansIdx);# print("-->", people[ansIdx], ansIdx)
                    N -= 1

                ans += 1

            elif limit == people[i]:
                # the current person weighs exactly the limit
                ans += 1

            i += 1
        
        # print("Final : ", people, N, i)
        return ans
        """

        # Using a greedy solution
        people.sort()
        N = len(people)
        l, r = 0, N-1
        ans = 0
        
        while l <= r:
            # Move to the next heavier person starting iteration with the most heaviest person & moving to lighter person
            weightRemain = limit - people[r]; #print(people, l, r, people[l], people[r], weightRemain)
            r -= 1

            # match both 'l' & 'r' people on same boat ~ people[l] is least heaviest person starting iteration from lightest person
            if (l <= r) and (people[l] <= weightRemain):
                ans += 1
                l += 1

            elif 0 <= weightRemain:
                ans += 1

            elif (r <= l) and (0 <= weightRemain):
                ans += 1

        return ans
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums = sorted(nums)
        ans = []

        # generate a prefix sum array where at each index 'i', the value stored is the sum of all 'i-1' elements
        sumArr = [0]
        # sumEle = 0

        for n in nums:
            # sumEle += n
            sumArr.append(sumArr[-1] + n) #sumArr.append(sumEle)
        
        N = len(sumArr); # print(sumArr)

        # perform Binary Search to find the length of sub-sequence of elements whose sum is less than equal to queries[i]
        # from the 'sumArr' - prefix sum array

        def BSearch(llim, ulim, ele):
            # use binary search to return the first element that is greater than the element we are searching for.
            while (llim < ulim):
                mid = llim + int((ulim - llim)/2)

                if sumArr[mid] < ele:
                    llim = mid+1

                elif ele < sumArr[mid]:
                    ulim = mid-1
                else:
                    break
            
            return mid
        
        # Linear Search Function Definition
        def LSearch(ele):
            i = 0

            while (i < N):
                if sumArr[i] < ele:
                    i += 1

                elif ele < sumArr[i]:
                    i -= 1
                    break
                
                else:
                    break
            
            return i if (i < N) else i-1


        for q in queries:
            # ans.append( BSearch(0, N-1, q) )
            idx = bisect.bisect_right(sumArr, q) # BInary Search Alternative -> use Python defined algorithm
            ans.append(idx - 1)
            # ans.append( LSearch(q) )

        return ans

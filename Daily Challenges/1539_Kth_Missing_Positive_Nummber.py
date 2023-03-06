class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        """
        # the array length can be atmost 1000 & value of k can be 1000 as per question
        # maintain a cache of boolean values whether the array item is present or not
        
        cache = [ False for i in range(2001) ]

        # the i-1 index stores whether the number i is present in passed array or not
        for num in arr:
            cache[num-1] = True
        i = 0
        ans = None
        while k:
            if not cache[i]:
                ans = i + 1
                k -= 1
            i += 1
        
        return ans
        """
        # Better Solution -> 
        #
        # Use Binary Search to find the position where the number of elements missing is greater than k
        # we can do so by getting the diff between the number stored at index i & the number to be
        # actually stored at index i had there been no missing elements i.e. i+1. -> 
        # this difference tells us the cumulative number of elements missing till index i.
        # 
        # Using binary search we should find the first position where the number of missing elements
        # till that position exceeds k ~ let that position be 'p' where k < (arr[p] - (p+1))
        # the from the elemnt stored at (p-1) we get the kth element which is our answer i.e.
        # the missing number : arr[p-1] + (k - (arr[p-1] - (p+1)) - 1)

        low, high = 0, len(arr)-1
        mid = None
        while low <= high:
            mid = low + (high-low)//2
            if  (arr[mid] - (mid + 1)) < k:
                # The first instance where the diff is greater than 'k' ~ that means
                # the missing element falls in the position of arr[mid]
                low = mid + 1
            else:
                high = mid - 1
        
        return low + k
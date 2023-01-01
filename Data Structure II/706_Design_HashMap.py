class MyHashMap:

    def __init__(self):
        """
            - Both the Key & values are integers - and keys are distinct
            - If identical keys are inserted consecutively, the corresponding value get updated
              and it doesn't accummulate.
            - Idea is to make the 'Key' a minHeap ~ so that it remains sorted & its easy to update
            - We'll map the Key with corresponding value by maintaining a list of [key, value]
              and Heap sorts it on the basis of the key
            - we'll have to search for the key on 'get' command ~so we need Binary / Linear Search algo which
              will be pretty fast to search the Key as the list will be partially sorted
            - remove -> Binary Search to get the Key -> obtain index & delete the list [key, value]
        """
        self.hashKeyValue = []
        self.N = 0 # size of the HashMap

    def put(self, key: int, value: int) -> None:
        #print("Put")

        if self.N == 0:
            # if no elements are in hash
            heapq.heappush(self.hashKeyValue, [key, value])
            self.N += 1 # updating the size of the hashMap
        else:
            # check if the key exists in the Hash then update the value or else do a simple push
            idx = self.BSearch(key)

            if idx == -9999:
                # Key does not exist in Hash
                heapq.heappush(self.hashKeyValue, [key, value])
                self.N += 1 # updating the size of the hashMap
            else:
                # Key exists in Hash & we update the corresponding value
                # No need to update the Size of the Heap
                self.hashKeyValue[idx][1] = value
        return
        
    def BSearch(self, key: int) -> int:
        
        """
        # Use binary Search to return the index of the key-element
        # Binary Search is might not work as the Heap is partially sorted / ordered structure
        # & it is not a completely sorted structure

        l, h = 0, self.N-1
        mid = int(l + (h-l)/2); #print(self.hashKeyValue)

        while l <= h:
            #print(mid, l, h, key, self.hashKeyValue[mid])
            mid = int(l + (h-l)/2); #l + int((h-l)/2)

            if self.hashKeyValue[mid][0] == key:
                break
            elif self.hashKeyValue[mid][0] < key:
                l = mid + 1
            else:
                h = mid - 1
        
        #print("-------------------------------", mid, key)
        # """
        
        # Use Linear Search to return the index of the key-element as Binary Search might not work
        mid = 0
        for idx, (k, v) in enumerate(self.hashKeyValue):
            if k == key:
                mid = idx
                break
        
        # check if Key exists in Hash
        if (mid < 0) or (self.N <= mid):
            mid = -9999
        elif self.hashKeyValue[mid][0]!=key:
            mid = -9999
        
        return mid
        
    def get(self, key: int) -> int:
        #print("Get")

        idx = self.BSearch(key)
        val = -1
        val = self.hashKeyValue[idx][1] if idx != -9999 else val
        
        return val


    def remove(self, key: int) -> None:
        #print("Remove")

        if self.N == 0:
            # No elements to delete
            return

        idx = self.BSearch(key)
        # remove the (key, value) tuple if it exists
        if idx != -9999:
            self.hashKeyValue.pop(idx)

            # ensure the heap invariant is mainatained by pushing and popping a -ve element
            # as problem constraint is that all keys are +ve
            heapq.heappushpop(self.hashKeyValue, [-1, -1])

            self.N -= 1 # Updating the size

        return

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
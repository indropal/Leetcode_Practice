class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if 2 <= len(nums):
            # If the number of elements in array is more than 1 ~ initialise sorting
            # perform Insertion Sort

            for i in range(1, len(nums)):
                j = i - 1
                key = nums[i]

                while 0 <= j and key < nums[j]:
                    nums[j+1] = nums[j]
                    j -= 1
                
                # Plae the key after the element smaller than it
                nums[j+1] = key
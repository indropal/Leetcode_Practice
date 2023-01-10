# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # recursively construct a binary search tree - root node is always 
        # greater than left-child but smaller than right child
        # use the sorted array & start with the middle element as the root
        # of the tree - the portion of array left of mid-element is samller
        # & corresponds to left sub tree while portion to the right of middle element is
        # greater and corresponds to right subtree.
        # for each sub portions of the array construct the tree by finding the mid-element
        # in sub-portion of array and constructin left & right sub-trees
        if len(nums) == 0:
            return None

        # find the mid-point of the array ~ this becomes the root node
        N = len(nums)
        mid = N//2

        # the left portion of the array is left-subtree & right portion is right subtree
        root = TreeNode(val = nums[mid])
        
        root.left = self.sortedArrayToBST(nums[:mid])

        if mid < N - 1:
            root.right = self.sortedArrayToBST(nums[mid+1:])
        else:
            root.right = None
        
        return root


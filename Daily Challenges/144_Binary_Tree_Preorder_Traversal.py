# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        # This is a recursive solution.
        if not root:
            return []
        # Recursively iterate through root followed by left sub-tree then right sub-tree
        return [root.val] + self.preorderTraversal(root.left) + self.preorderTraversal(root.right)
        """
        
        if not root:
            return []

        # Solve this iteratively
        ans = []
        stack = [root] # maintain a stack - LIFO

        while stack:
            # for each iteration till stack is not empty, pop the node on top of stack
            # take the popped node & include it into answer array
            # We know Stack is LIFO structure & Preorder traversal is : node-> left->right
            # take the right-child node of popped node & include into stack & then do
            # the same for left-child node is any of the nodes exist
            # Why we push the right node before the left node ??
            # >> We do so in order to ensure that the left-child node gets popped out before the 
            #    the right-child node thereby adhering to Preorder traversal, since stack is LIFO.

            node = stack.pop()
            ans.append(node.val)

            if node.right:
                # if right-child node exists, include into stack
                stack.append(node.right)
            
            if node.left:
                # if left-child node exists, include into stack
                stack.append(node.left)
        
        return ans
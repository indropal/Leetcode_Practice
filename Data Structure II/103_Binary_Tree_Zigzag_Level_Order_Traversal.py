# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode], bin=True) -> List[List[int]]:
        if not root:
            return []
        
        # Do Depth first search on the tree ~ at each iteration we'll be going
        # through each level of the  Binary Tree i.e. hierarchy wise
        # The initial traversal from th root node is from left-to-right
        queue, ans = [root], [[root.val]]
        tmpAns = []
        nextQ = []
        binTraverse = True # flag signifying right-to-left traversal

        while queue:

            node = queue.pop(0)

            # Include the Right Child Node first as after the root node
            # we are traversing in Right-to-Left order which will change
            # to left-to-right order for the next tree level ~ this order
            # will alternate for subsequent tree-levels
            if node.right: nextQ.append(node.right)
            if node.left: nextQ.append(node.left)

            # include in answer ~ the child node values
            if node.right: tmpAns.append(node.right.val)
            if node.left: tmpAns.append(node.left.val)
            
            # print([q.val for q in queue], tmpAns, binTraverse)

            if len(queue) == 0:
                # assign a copy of nextQ as queue get updated with nextQ
                # we want queue & nextQ to be different and not the same List object
                queue = nextQ[:]
                nextQ = []

                # Only include the ans if it is non-empty
                if not binTraverse and tmpAns:
                    # reverse the Answer array for subsequent level/heierarchy of tree
                    ans.append(tmpAns[::-1])
                elif tmpAns:
                    ans.append(tmpAns)
                
                tmpAns = []
                binTraverse = not binTraverse

        return ans
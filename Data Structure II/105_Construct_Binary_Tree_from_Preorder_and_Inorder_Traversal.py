# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        # Preorder traversal involves : Root -> left-subtree -> right-subtree
        # Inorder traversal involves : left-subtree -> Root -> right-subtree
        # The first element in Preorder array is the root node ~ the second element
        # in Ppreorder array will be the root node of the left-subtree
        # Likewise, the first element in Inorder traversal is the left-most node in the Tree
        #
        # We need to first find the first node of Preorder-traversal (root node) array in the
        # Inorder traversal array - everything before this node in the Inorder traversal array
        # belongs to the left-subtree and everything after this node is the right subtree.
        # We obtain these subtree segments in Inorder traversal array from the Preorder array
        # which become the respective subtrees & their first elements are the root of the 
        # subtrees ~ we continue sugmenting the arrays & isolating the subtrees until the array
        # segments are of zero length thus meaning we have reached the leaf nodes
        # 
        # We perform this logic recursively.
        # We can use this logic as we are guaranteed that the trversal arrays & tree elements do 
        # not have repeated values - all are unique

        if not preorder or not inorder:
            # if any of the traversal lists are empty ~ return
            return None
        
        # print("-->>", inorder, preorder)
        
        # obtain the root-node of (sub)tree
        root = TreeNode(val=preorder[0])
        # find the relevant root element index in Inorder list
        rootIdx = inorder.index(root.val)
        
        # all elements before this Index belongs to the left subtree
        leftSubTreeInorder = inorder[:rootIdx]
        # Get number of elements in left-SubTree
        leftTreeN=len(leftSubTreeInorder)
        # print("Inorder LeftSubtree:", leftSubTreeInorder, leftTreeN)

        # all elements after the root-indez belongs to the right subtree
        rightSubTreeInorder = []
        if rootIdx < (len(inorder)-1):
            rightSubTreeInorder = inorder[rootIdx+1:]
        
        rightTreeN = len(rightSubTreeInorder)
        # print("Inorder RightSubtree:", rightSubTreeInorder, rightTreeN)

        # From the Preorder traversal array, get the left-subtree portion
        # which follow right after the root-node and is of length 'leftTreeN'
        leftSubTreePreorder = preorder[1:leftTreeN+1]

        # The segment after [1:'leftTreeN'] is the right subtree portion which
        # is of length 'rightTreeN'
        rightSubTreePreorder = preorder[1+leftTreeN:1+leftTreeN+rightTreeN]
        
        # print("Preorder leftSubTree:", leftSubTreePreorder)
        # print("Preorder rightSubTree:", rightSubTreePreorder)

        # Get the left & right child nodes respectively
        # pass left subTree
        root.left = self.buildTree(preorder=leftSubTreePreorder, inorder=leftSubTreeInorder) 
        # pass right subTree
        root.right = self.buildTree(preorder=rightSubTreePreorder, inorder=rightSubTreeInorder)

        return root
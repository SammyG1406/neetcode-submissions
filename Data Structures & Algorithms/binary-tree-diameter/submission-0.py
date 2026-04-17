# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        #traverse the children 
        # finding the maximum depth but less 1
        self.count = 0

        def findMax(root):
            if not root:
                return 0
            else:
                leftDiameter = findMax(root.left)
                rightDiameter = findMax(root.right)
                self.count = max(self.count, leftDiameter + rightDiameter)
                return 1 + max(leftDiameter, rightDiameter)

        findMax(root)
        return self.count
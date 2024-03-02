# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (node.val < right and node.val > left):
                return False
            leftR = valid(node.left,left,node.val)
            rightR = valid(node.right,node.val,right)
            return leftR and rightR
        return valid(root, float("-inf"),float("inf"))
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        valToNode = {}

        for p, c, isLeft in descriptions:
            parent = valToNode.setdefault(p, TreeNode(p))
            child = valToNode.setdefault(c, TreeNode(c))
            if isLeft:
                parent.left = child
            else:
                parent.right = child
            children.add(c)
        root = (set(valToNode) - set(children)).pop()
        return valToNode[root]
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        
        q = collections.deque()
        q.append(root)

        return [[0], [0]]


print(levelOrder(TreeNode(1, TreeNode(2), TreeNode(3))))
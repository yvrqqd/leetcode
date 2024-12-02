# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0

        def g(s1, lp):
            nonlocal total

            new_st = s1 + str(lp.val)

            if lp.right is not None:
                g(new_st, lp.right)

            if lp.left is not None:
                g(new_st, lp.left)

            elif lp.right is None and lp.left is None:
                total += int(new_st)

        g('', root)

        return total

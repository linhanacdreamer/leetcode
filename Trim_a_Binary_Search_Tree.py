# Definition for a binary tree node.
from lhTree  import TreeNode

class Solution(object):
    '''
        对于L来说，
            如果结点的  val < L 那么 这个结点就应该被替换掉，
                因此 这个结点 = 找到最小的val >= L的结点,就得往该结点的右子树中寻找
            如果结点的  val >= L 那么 这个结点应该被保留，
                那么 要寻找>=L的最小值只能在 这个结点的左子树里面
                因此 这个结点.left = 找到的val >= L的结点
    '''
    def findLeft(self,root,L,str):
        if not root:
            return None
        if root.val >= L:
            root.left = self.findLeft(root.left,L,str + ' ')
        elif root.val < L:
            root = self.findLeft(root.right,L, str + ' ')
        return root
    '''
        对于R来说，
            如果结点的  val > R 那么 这个结点就应该被替换掉，
                因此 这个结点 = 找到最大的val <= R的结点,就得往该结点的左子树中寻找
            如果结点的  val <=  R 那么 这个结点应该被保留，
                那么 要寻找<=R的最大值只能在 这个结点的右子树里面
                因此 这个结点.right = 找到的val <= R的结点
    '''
    def findRight(self,root,R,str):
        if not root:
            return None
        if root.val > R:
            root = self.findRight(root.left,R,str + ' ')
        elif root.val <= R:
            root.right = self.findRight(root.right,R, str + ' ')
        return root

    def trimBST(self, root, L, R):
        return self.findRight(self.findLeft(root,L,''),R,'')

# Definition for a binary tree node.
'''
        if not (t1 and t2):
            return t1 or t2
        queue1, queue2 = collections.deque([t1]), collections.deque([t2])
        while queue1 and queue2:
            node1, node2 = queue1.popleft(), queue2.popleft()
            if node1 and node2:
                node1.val = node1.val + node2.val
                if (not node1.left) and node2.left:
                    node1.left = TreeNode(0)
                if (not node1.right) and node2.right:
                    node1.right = TreeNode(0)
                queue1.append(node1.left)
                queue1.append(node1.right)
                queue2.append(node2.left)
                queue2.append(node2.right)
        return t1

        if not t1 and not t2:
            return None
        q1, q2 = collections.deque([t1]), collections.deque([t2])
        root = TreeNode(0)
        q = collections.deque([root])
        while q1 and q2:
            node1, node2, node = q1.popleft(), q2.popleft(), q.popleft()
            node.val = (node1 and node1.val or 0) + (node2 and node2.val or 0)
            if (node1 and node1.left) or (node2 and node2.left):
                q1.append(node1 and node1.left)
                q2.append(node2 and node2.left)
                node.left = TreeNode(0)
                q.append(node.left)
            if (node1 and node1.right) or (node2 and node2.right):
                q1.append(node1 and node1.right)
                q2.append(node2 and node2.right)
                node.right = TreeNode(0)
                q.append(node.right)
        return root

    if t1 == None:
        return t2
    if t2 == None:
        return t1
    else:
        t1.val += t2.val
    t1.left = self.mergeTrees(t1.left, t2.left)
    t1.right = self.mergeTrees(t1.right, t2.right)
    return t1

    if not t1:
            return t2
        if t2:
            t1.val += t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t1.right = self.mergeTrees(t1.right, t2.right)
        return t1


    if not t1 and not t2: return None
    ans = TreeNode((t1.val if t1 else 0) + (t2.val if t2 else 0))
    ans.left = self.mergeTrees(t1 and t1.left, t2 and t2.left)
    ans.right = self.mergeTrees(t1 and t1.right, t2 and t2.right)
    return ans

        if t1 and t2:
            root = TreeNode(t1.val + t2.val)
            root.left = self.mergeTrees(t1.left, t2.left)
            root.right = self.mergeTrees(t1.right, t2.right)
            return root
        else:
            return t1 or t2

        if not t1 and not t2: return None
        if t1:
            v1, L1, R1 = t1.val, t1.left, t1.right
        else:
            v1, L1, R1 = 0, None, None
        if t2:
            v2, L2, R2 = t2.val, t2.left, t2.right
        else:
            v2, L2, R2 = 0, None, None
        node = TreeNode(v1+v2)
        node.left = self.mergeTrees(L1, L2)
        node.right = self.mergeTrees(R1, R2)
        return node



class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t2 :
            return t1
        else:
            if t1:
                t1.val = t2.val + t1.val
                if t2.left:
                    if t1.left:
                        self.mergeTrees(t1.left, t2.left)
                    else:
                        t1.left = t2.left
                if t2.right:
                    if t1.right:
                        self.mergeTrees(t1.right,t2.right)
                    else:
                        t1.right = t2.right
            else:   # t1 is null
                t1 = t2
        return t1
'''
class TreeNode(object):
    def __init__(self, x):# it doesn't allow new attributes
        self.val = x
        self.left = None
        self.right = None
        self.flag = False
        self.father = None
class Solution(object):
    def mergeTrees(self, t1, t2):
        if not t1:
            return t2
        if not t2 :
            return t1
        tmpt1 = t1
        tmpt2 = t2
        while tmpt2:
            if tmpt2.flag:
                tmpt2 = tmpt2.father
                tmpt1 = tmpt1.father
                continue
            if tmpt1:
                if tmpt2.left:
                    if not tmpt2.left.flag:
                        if tmpt1.left:
                            #self.mergetrees(tmpt1.left, tmpt2.left)
                            tmpt2.left.father = tmpt2
                            tmpt2 = tmpt2.left
                            tmpt1.left.father = tmpt1
                            tmpt1 = tmpt1.left
                            continue
                        else:
                            tmpt1.left = tmpt2.left
                    else:
                        pass
                if tmpt2.right:
                    if not tmpt2.right.flag:
                        if tmpt1.right:
                            #self.mergeTrees(tmpt1.right,tmpt2.right)
                            tmpt2.right.father = tmpt2
                            tmpt2 = tmpt2.right
                            tmpt1.right.father = tmpt1
                            tmpt1 = tmpt1.right
                            continue
                        else:
                            tmpt1.right = tmpt2.right
                    else:
                        pass
                tmpt1.val = tmpt2.val + tmpt1.val
                tmpt2.flag = True
            else:
                tmpt1 = tmpt2
                tmpt2.flag = True
        return t1

# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-06-14 14:33:18
# @Last modified by:   WuLC
# @Last Modified time: 2016-06-14 14:33:33
# @Email: liangchaowu5@gmail.com

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if root == None: return result
        self.helper([root], result)
        return result
        
    def helper(self, nodes, result):
        if len(nodes) == 0: return
        next_level, tmp = [], []
        for i in xrange(len(nodes)):
            tmp.append(nodes[i].val)
            if nodes[i].left:
                next_level.append(nodes[i].left)
            if nodes[i].right:
                next_level.append(nodes[i].right)
        result.append(tmp)
        self.helper(next_level, result)

# another kind of recursive method
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []
        result = [[root.val]]
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        i = 0
        while i < len(left) and i < len(right):
            result.append(left[i] + right[i])
            i += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while i < len(right):
            result.append(right[i])
            i += 1
        return result
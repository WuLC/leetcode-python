# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2016-10-25 21:24:59
# @Last modified by:   WuLC
# @Last Modified time: 2016-10-27 22:21:50
# @Email: liangchaowu5@gmail.com


# DFS
# try to reach as far as possible at each position, when reach the edge return true
# long and ugly code, though with DP, sitll TLE
class Solution(object):
    
    def __init__(self):
        self.top = None
        self.bottom = None
        self.left = None
        self.right = None
        self.visited = None
        self.dp = None
    
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        m = len(matrix)
        if m==0:
            return result
        n = len(matrix[0])
        self.visited = [[0 for j in xrange(n)] for i in xrange(m)]
        self.dp = [[False for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                self.top = self.bottom = i
                self.left = self.right = j
                if (i>0 and matrix[i][j] >= matrix[i-1][j] and self.dp[i-1][j]) or (j>0 and matrix[i][j] >= matrix[i][j-1] and self.dp[i][j-1]) or self.dfs(matrix, i, j, m, n):
                    self.dp[i][j] = True
                    result.append([i,j])
        return result
        
    def dfs(self, matrix, i, j, m, n):
        if (self.top == 0 or self.left == 0) and (self.right == n-1 or self.bottom == m-1):
            return True
        self.visited[i][j] = 1
        if i-1 >= 0 and  self.visited[i-1][j] == 0 and matrix[i][j] >= matrix[i-1][j]:
            if self.top > i-1:
                self.top = i-1
            if self.dfs(matrix, i-1, j, m, n):
                self.visited[i][j] = 0
                return True
        if j-1 >= 0 and self.visited[i][j-1] == 0 and matrix[i][j] >= matrix[i][j-1]:
            if self.left > j-1:
                self.left = j-1
            if self.dfs(matrix, i, j-1, m, n):
                self.visited[i][j] = 0
                return True
        if i+1 < m and self.visited[i+1][j] == 0 and matrix[i][j] >= matrix[i+1][j]:
            if self.bottom < i+1:
                self.bottom = i+1
            if self.dfs(matrix, i+1, j, m, n):
                self.visited[i][j] = 0
                return True
        if j+1 < n and self.visited[i][j+1] == 0 and matrix[i][j] >= matrix[i][j+1]:
            if self.right < j+1:
                self.right = j+1
            if self.dfs(matrix, i, j+1, m, n):
                self.visited[i][j] = 0
                return True
        self.visited[i][j] = 0
        
    


# DFS
# referer: https://discuss.leetcode.com/topic/62379/java-bfs-dfs-from-ocean
# use two visit matrix, one for pacific and the other for atlantic
# for either ocean, from the edge of ocean to reach any positioin that it can reach and update the visited table
# finally, the positions that can be visited in both visite table is the positions that can visit both ocean

class Solution(object):
    moves = ((0,1), (0,-1), (1,0), (-1,0))
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        m = len(matrix)
        if m == 0:
            return result
        n = len(matrix[0])
        p_visited = [[0 for j in xrange(n)] for i in xrange(m)]
        a_visited = [[0 for j in xrange(n)] for i in xrange(m)]
        for i in xrange(m):
            self.dfs(i, 0, m, n, matrix, p_visited)
            self.dfs(i, n-1, m, n, matrix, a_visited)
        for j in xrange(n):
            self.dfs(0, j, m, n, matrix, p_visited)
            self.dfs(m-1, j, m, n, matrix, a_visited)
             
        for i in xrange(m):
            for j in xrange(n):
                if p_visited[i][j] == 1 and a_visited[i][j] == 1:
                    result.append([i, j])
        return result
        
    def dfs(self, i, j, m, n, matrix, visited):
        visited[i][j] = 1
        for move in Solution.moves:
            x, y = i+move[0], j+move[1]
            if 0<=x<m and 0<=y<n and visited[x][y] == 0 and matrix[i][j] <= matrix[x][y]:
                self.dfs(x, y, m, n, matrix, visited)
        
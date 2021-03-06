# -*- coding: utf-8 -*-
# @Author: WuLC
# @Date:   2017-08-15 09:49:48
# @Last Modified by:   WuLC
# @Last Modified time: 2017-08-15 16:33:43


# stack with penalty, penalty is to increment the start time of the functions that are still in the stack
# average time complexity: O(n^2)
class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack  = []
        result = [0 for _ in xrange(n)]

        for log in logs:
            id, flag, time = log.split(':')
            id, time = int(id), int(time)
            if flag == 'start':
                stack.append(time)
            else:
                delta = time - stack.pop() + 1
                result[id] += delta
                for i in xrange(len(stack)):
                    stack[i] += delta
        return result
                
                
                
# more efficient stack
# any start means the end of the previous function

class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        stack  = []
        result = [0 for _ in xrange(n)]
        prev = 0
        for log in logs:
            id, flag, time = log.split(':')
            id, time = int(id), int(time)
            if flag == 'start':
                if len(stack) > 0:
                    result[stack[-1]] += time - prev
                stack.append(id)
                prev = time
            else:
                result[stack.pop()] += time - prev + 1
                prev = time + 1
        return result
                    
                    
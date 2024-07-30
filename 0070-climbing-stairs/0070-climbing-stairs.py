class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        1, 2, 3, 5
        
        '''
        if n <= 2:
            return n
        prev, cur = 1, 2
        for i in range(3, n + 1):
            next = prev + cur
            prev, cur = cur, next
        return cur
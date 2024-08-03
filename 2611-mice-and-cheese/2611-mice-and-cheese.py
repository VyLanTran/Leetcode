class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        '''
        reward1 = 1,1,3,4
        reward2 = 4,4,1,1
        diff    = -3, -3, 2, 3
        
        1, 1
        1, 1
        0, 0
        
        '''
        
        n = len(reward1)
        diff = [reward1[i] - reward2[i] for i in range(n)]
        maxHeap = [(-diff[i], i) for i in range(n)]
        heapify(maxHeap)
        res = 0
        for i in range(k):
            (_, j) = heappop(maxHeap)
            res += reward1[j]
        while maxHeap:
            (_, j) = heappop(maxHeap)
            res += reward2[j]
        return res
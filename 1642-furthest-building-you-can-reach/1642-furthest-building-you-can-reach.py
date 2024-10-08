class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        n = len(heights)
        minHeap = []
        i = 0
        while i < n:
            if i == n - 1:
                return i
            diff = heights[i + 1] - heights[i]
            if diff <= 0:
                i += 1
                continue
            heappush(minHeap, diff)
            if len(minHeap) > ladders:
                minDiff = heappop(minHeap)
                if minDiff > bricks:
                    return i
                bricks -= minDiff
            i += 1
        return i
        
#         n = len(heights)
#         left, right = 0, n - 1
        
#         def canReach(lastBuilding):
#             arr = []
#             for i in range(lastBuilding):
#                 diff = heights[i + 1] - heights[i]
#                 if diff > 0:
#                     arr.append(diff)
#             arr.sort(reverse = True)
#             sum = 0
#             for i in range(ladders, len(arr)):
#                 sum += arr[i]
#                 if sum > bricks:
#                     return False
#             return True
                
#         while left <= right:
#             mid = left + (right - left) // 2
#             if not canReach(mid):
#                 right = mid - 1
#             elif mid == n - 1 or not canReach(mid + 1):
#                 return mid
#             else:
#                 left = mid + 1
                
#         return n - 1

            
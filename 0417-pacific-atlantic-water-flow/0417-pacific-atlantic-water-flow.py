class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        visited = [[[False, False] for _ in range(cols)] for _ in range(rows)]
        res = []
        
        def dfs(i, j, oceanIndex, prevHeight):
            if i < 0 or j < 0 or i >= rows or j >= cols or visited[i][j][oceanIndex] or heights[i][j] < prevHeight:
                return
            visited[i][j][oceanIndex] = True
            if oceanIndex == 1 and visited[i][j] == [True, True]:
                res.append([i, j])
            dfs(i - 1, j, oceanIndex, heights[i][j])
            dfs(i + 1, j, oceanIndex, heights[i][j])
            dfs(i, j - 1, oceanIndex, heights[i][j])
            dfs(i, j + 1, oceanIndex, heights[i][j])
            
        for i in range(rows):
            for j in range(cols):
                if i == 0 or j == 0:
                    dfs(i, j, 0, -1)
                    
        for i in range(rows):
            for j in range(cols):
                if i == rows - 1 or j == cols - 1:
                    dfs(i, j, 1, -1)
                    
        return res
        
        # tup1 = [True, True]
        # print(tup1 == [True, True])
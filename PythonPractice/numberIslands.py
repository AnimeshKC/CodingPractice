#leetcode question 
class Solution:
    '''Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

'''
    counter = 0 
    def numIslands(self, grid: List[List[str]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    self.counter += 1
                    self.clearIsland(grid, i, j)
        return self.counter
    def clearIsland(self, grid, i, j):
        if i < 0 or i >= len(grid)  or j < 0 or j >= len(grid[i]):
            return
        elif grid[i][j] == "0":
            return
        grid[i][j] = "0"
        self.clearIsland(grid, i, j-1)
        self.clearIsland(grid, i-1, j)
        self.clearIsland(grid, i, j+1)
        self.clearIsland(grid, i+1, j)
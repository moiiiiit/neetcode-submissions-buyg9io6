class Solution:
    def explore(self, grid: List[List[str]], index1: int, index2: int):
        if index1 < 0 or index2 < 0 or index1 >= len(grid) or index2 >= len(grid[0]):
            return
        if grid[index1][index2] == "1" and not self.visited[index1][index2]:
            self.visited[index1][index2] = 1
            for offset in self.offsets:
                self.explore(grid, index1 + offset[0], index2 + offset[1])


    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0
        self.offsets = [
            (1,0), (0,1), (-1, 0), (0, -1)
        ]
        self.visited = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        for index1 in range(len(grid)):
            for index2 in range(len(grid[0])):
                element = grid[index1][index2]
                if element == "1" and not self.visited[index1][index2]:
                    num_islands += 1
                    print(index1, index2)
                    self.explore(grid, index1, index2)
        return num_islands

class Solution:
    def numIslands(self, grid) -> int:
        width = len(grid)
        height = len(grid[0])
        count = 0

        def expandAndClean(x, y):
            if x < 0 or x >= width or y < 0 or y >= height:
                return

            if grid[x][y] == "0":
                return

            if grid[x][y] == "1":
                grid[x][y] = "0"
                expandAndClean(x + 1, y)
                expandAndClean(x - 1, y)
                expandAndClean(x, y + 1)
                expandAndClean(x, y - 1)

        for i in range(0, width):
            for j in range(0, height):
                if grid[i][j] == "1":
                    count += 1
                    # if I find any island, spread 0 so this island disappear from the grid 
                    expandAndClean(i, j)

        return count


def check(grid, ans):
    result = (Solution()).numIslands(grid)
    print(result, result == ans)


check([["1", "1"], ["1", "1"]], 1)
check([["1", "0"], ["0", "1"]], 2)
check([["1", "1"], ["1", "0"]], 1)
check([["0"]], 0)
check(
    [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ],
    1,
)
check(
    [
        ["1", "1", "0", "0", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "1", "0", "0"],
        ["0", "0", "0", "1", "1"],
    ],
    3,
)

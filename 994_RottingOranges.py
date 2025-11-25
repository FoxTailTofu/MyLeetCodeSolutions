from collections import deque


class Solution:
    def orangesRotting(self, grid) -> int:
        width = len(grid)
        height = len(grid[0])
        rotting = deque()

        fresh = 0 # a fresh counter to fast check if any fresh orange left after rotten
        timer = 0

        # find all initial rotting oranges
        for i in range(0, width):
            for j in range(0, height):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    rotting.append([i, j])

        # foreach initial rotting oranges
        # spread rotten, push all the rotten into next iteration
        # add 1 minutes to timer if spread happens
        # i'll use [-1,-1] as a marker for one iteration is done
        offset = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        nextIter = False
        while len(rotting):
            x, y = rotting.popleft()

            if x == -1 and y == -1:
                nextIter = False
                timer += 1

            for ox, oy in offset:
                if not (0 <= x + ox < width and 0 <= y + oy < height):
                    continue

                if grid[x + ox][y + oy] != 1:
                    continue

                # ok we find something to rotten this iteration
                if not nextIter:
                    rotting.append([-1, -1])  # mark it
                    nextIter = True  # make sure no duplicated mark

                grid[x + ox][y + oy] = 2
                rotting.append([x + ox, y + oy])
                fresh -= 1


        # ! we have a fresh variable that does this for me
        # test if any orange is still not rotting
        # we already loop though the array once, so this doesn't add more time complexity
        # for i in range(0, width):
        #     for j in range(0, height):
        #         if grid[i][j] == 1:
        #             return -1

        return timer if fresh == 0 else -1

    # NeetCode https://www.youtube.com/watch?v=y704fEOx0s0
    def orangesRotting_Neetcode(self, grid):
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                # we just record how many fresh there is so I don't do another loop
                if grid[r][c] == 1:
                    fresh += 1
                # still log all the coord that have rotten orange
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):  # the iteration marker
                r, c = q.popleft()
                for dr, dc in directions:
                    row, col = r + dr, c + dc

                    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
                        continue  # out of bound

                    if grid[row][col] != 1:
                        continue  # not fresh, don't care

                    # ok we got something fresh, we rotten it
                    grid[row][col] = 2
                    q.append([row, col])

                    fresh -= 1
            time += 1
        return time if fresh == 0 else -1


def check(grid, ans):
    result = (Solution()).orangesRotting(grid)
    print(result, result == ans)


check([[2, 1, 1], [1, 1, 0], [0, 1, 1]], 4)
check([[2, 1, 1], [0, 1, 1], [1, 0, 1]], -1)
check([[0, 2, 2]], 0)
check([[2, 2, 2, 1, 1]], 2)
check([[2, 2], [1, 1], [0, 0], [2, 0]], 1)

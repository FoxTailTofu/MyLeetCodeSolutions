class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        moves = [[1,0],[0,1],[-1,0],[0,-1]]
        move = 0
        d = 0
        x = 0
        y = 0

        result = []
        while left <= right and top <= bottom:
            print(x,y,left,right,d,result)
            result.append(matrix[y][x])
            if d == 0 and x >= right:
                top+=1
                d = 1
            elif d == 1 and y >= bottom:
                right-=1
                d = 2
            elif d == 2 and x <= left:
                bottom-=1
                d = 3
            elif d == 3 and y <= top:
                left+=1
                d = 0

            x += moves[d][0]
            y += moves[d][1]

        return result

res = (Solution()).spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print(res)
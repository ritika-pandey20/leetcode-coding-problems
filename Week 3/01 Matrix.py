class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]: 
        
        ##Using BFS
        
        m = len(mat[0])
        n = len(mat)
        q = []

        for i in range(n):
            for j in range(m):
                if mat[i][j] == 0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1

        for row, col in q:
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr = row + dx
                nc = col + dy
                if 0<=nr<n and 0<=nc<m and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[row][col] + 1
                    q.append((nr, nc))
        return mat


    # Time complexity-- O(r c)
    # Space Complexity-- O(r c)
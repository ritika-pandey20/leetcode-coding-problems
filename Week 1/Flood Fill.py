class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if(image[sr][sc]==color):
            return image
        temp=image[sr][sc]
        stack=[(sr,sc)]
        while(stack):
            i,j=stack.pop()
            if(image[i][j]==temp):
                image[i][j]=color    
                if(i+1<len(image)):
                    stack.append((i+1,j))
                if(i-1>=0):
                    stack.append((i-1,j))
                if(j+1<len(image[0])):
                    stack.append((i,j+1))
                if(j-1>=0):
                    stack.append((i,j-1))
            else:
                pass
        return image
'''
    My Solution: Start with a left and right pointer, setting the boundaries of the cubic 
    matrix. We start with the outer ring of elements. We first save the top left element 
    in a variable. 
        The top left element equals to the bottom left element. 
        The bottom left equals to the bottom right.
        The bottom right equals to the top right.
        The top right equals to the original top left stored in the variable.
    We then iterate to the element next to the top left and repeat the above process, 
    except the elements we're looking at are no shifted:
        The current element now equals to the bottom left shifted up 1.
        The bottom left shifted up equals to the bottom right shifted left 1.
        The bottom right shifted left equals to the top right shifted down 1.
        The top right shifted down equals to the variable.
    Interpret it as if with each element we've currently iterated at, rotate the rest of 
    the matrix we are observing by 1.

    We repeat the same process for the inner layers (by minimizing the left and right 
    pointer window) until they cross.

    Time Complexity: O(nlogn)
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix)-1
        
        while l < r:
            for i in range(r-l):
                t, b = l, r
                top_left = matrix[t][l+i]
                
                matrix[t][l+i] = matrix[b-i][l]
                matrix[b-i][l] = matrix[b][b-i]
                matrix[b][b-i] = matrix[t+i][b]
                matrix[t+i][b] = top_left
                
            l += 1
            r -= 1
            
        return matrix
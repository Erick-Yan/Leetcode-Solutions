class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        l, r = 0, len(matrix[0])-1
        t, b = l, len(matrix)-1
        ret = []
        
        while l <= r and t <= b:
            i = t
            
            while i <= r:
                ret.append(matrix[t][i])
                i += 1
            if i == t:
                break
            i = t+1
            while i <= b:
                ret.append(matrix[i][r])
                i += 1
            if i == t+1:
                break
            i = r-1
            while i >= l:
                ret.append(matrix[b][i])
                i -= 1
            if i == r-1:
                break
            i = b-1
            while i > t:
                ret.append(matrix[i][l])
                i -= 1
            
            l += 1
            r -= 1
            t += 1
            b -= 1
            
        return ret
                
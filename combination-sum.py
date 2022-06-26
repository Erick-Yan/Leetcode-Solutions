'''
    My Solution: Use backtracking. Inside the backtracking (DFS) function, if the current total from the sublist is equal to the target, we append it into a return list. If the current total 
    is less than the target and the current list index is less than the list length, we recursively call the backtracking function to find 2 options:
        1. Sublists with the current element appended and with the next element being the same one appended (covering case where we can use the same element multiple times).
        2. Sublists without the current element appended and with the next element being the next one in the list (covering sublists that start from another element).
'''

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def dfs(curr, i, total):
            if total == target:
                ret.append(curr.copy())
            if i < len(candidates) and total < target:
                curr.append(candidates[i])
                dfs(curr, i, total + candidates[i])
                curr.pop()
                dfs(curr, i + 1, total)  
            return
        dfs([], 0, 0)
        return ret
'''
    My Solution: Start with two pointers from both ends of the list. If the area is greater than the max 
    area, replace the max area. If the left pointer element is lower than the right power element, iterate from 
    the left until you arrive at an element with a larger value than the original left pointer value. If the right 
    pointer is lower than the left pointer element, do the opposite.
'''

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            lower = height[left] if height[left] < height[right] else height[right]
            area = lower * (right - left)
            if area > max_area:
                max_area = area
            if height[right] == lower:
                right -= 1
                while height[right] <= height[right + 1] and right > -1:
                    right -= 1
                continue
            if height[left] == lower:
                left += 1
                while height[left] <= height[left - 1] and left < len(height):
                    left += 1
        return max_area
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        ptr1=0
        ptr2=len(heights)-1
        while ptr1<ptr2:
            area = min(heights[ptr1], heights[ptr2]) * (ptr2-ptr1)
            if area>max_area:
                max_area = area
            if heights[ptr1] <= heights[ptr2]:
                ptr1 += 1
            else:
                ptr2 -= 1
        return max_area
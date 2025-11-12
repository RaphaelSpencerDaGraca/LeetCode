from typing import List
"""
The `maxArea` function calculates the maximum area that can be formed by selecting two lines from a
list of heights using a two-pointer approach.
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        This function calculates the maximum area that can be formed by selecting two lines from a list
        of heights.
        
        :param height: The `height` parameter in the `maxArea` function is a list of integers
        representing the heights of the vertical lines. The function calculates the maximum area that
        can be formed by selecting two lines from the list and forming a container with the x-axis. The
        function uses a two-pointer approach to find
        :type height: List[int]
        :return: The function `maxArea` is returning an integer value, which represents the maximum area
        of water that can be trapped between the vertical lines represented by the input list `height`.
        """
        left,right = 0,len(height)-1
        result = 0
        for i in range (len(height)-1):
            result = max(result, min(height[left],height[right])*(right-left))
            if (height[left]< height[right]):
                left +=1
            else:
                right-=1      
        return result
    

def test_containersWithMosterWater():
    sol = Solution()

    assert sol.maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert sol.maxArea([1,1]) == 1

if __name__ =="__main__":
    test_containersWithMosterWater()

    

from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
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

from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbersHashMap = {number: index for index, number in enumerate(numbers)}
        for index, values in enumerate(numbers):
            if target - values in numbersHashMap:
                return [index+1,numbersHashMap.get(target-values)+1]
        return []



def test_twoSum2():
    sol = Solution()

    assert sol.twoSum([2,7,11,15],9) == [1,2]
    assert sol.twoSum([2,3,4],6) == [1,3]
    assert sol.twoSum([-1,0],-1) == [1,2]


if __name__ == "__main__":
    test_twoSum2()
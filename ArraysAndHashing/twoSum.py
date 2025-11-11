from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for index, valeur in enumerate(nums):
            tmp = target - valeur
            if tmp in prevMap:
                return [prevMap[tmp], index]
            prevMap[valeur] = index
        return []

def test_twoSum_basic():
    sol = Solution()
    assert sol.twoSum([2, 7, 11, 15], 9) == [0, 1]
    print("Test 1 (cas classique) : OK")

def test_twoSum_no_solution():
    sol = Solution()
    assert sol.twoSum([1, 2, 3], 7) == []
    print("Test 2 (pas de solution) : OK")

def test_twoSum_multiple_solutions():
    sol = Solution()
    assert sol.twoSum([3, 2, 4], 6) == [1, 2]
    print("Test 3 (plusieurs solutions possibles) : OK")

if __name__ == "__main__":
    test_twoSum_basic()
    test_twoSum_no_solution()
    test_twoSum_multiple_solutions()

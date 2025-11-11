from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

def test_containsDuplicate_with_duplicates():
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 1]) == True
    print("Test 1 (avec doublons) : OK")

def test_containsDuplicate_no_duplicates():
    sol = Solution()
    assert sol.containsDuplicate([1, 2, 3, 4]) == False
    print("Test 2 (sans doublons) : OK")

def test_containsDuplicate_edge_cases():
    sol = Solution()
    assert sol.containsDuplicate([]) == False
    assert sol.containsDuplicate([1]) == False
    print("Test 3 (liste vide ou un seul élément) : OK")

if __name__ == "__main__":
    test_containsDuplicate_with_duplicates()
    test_containsDuplicate_no_duplicates()
    test_containsDuplicate_edge_cases()

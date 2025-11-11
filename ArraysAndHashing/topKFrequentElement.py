from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occurence = {}
        result = []
        for i in nums:
            if i in occurence:
                occurence[i] += 1
            else:
                occurence[i] = 1

        for j in range(k):
            key_max = max(occurence, key=occurence.get)
            result.append(key_max)
            del occurence[key_max]
        return result

def test_topKFrequent_basic():
    sol = Solution()
    assert sol.topKFrequent([1, 1, 1, 2, 2, 3], 2) == [1, 2]
    print("Test 1 (cas classique) : OK")

def test_topKFrequent_with_duplicates():
    sol = Solution()
    assert sorted(sol.topKFrequent([1, 1, 2, 2, 3, 3], 3)) == [1, 2, 3]
    print("Test 2 (tous les éléments ont la même fréquence) : OK")

def test_topKFrequent_edge_cases():
    sol = Solution()
    assert sol.topKFrequent([1], 1) == [1]
    assert sol.topKFrequent([-1, -1], 1) == [-1]
    print("Test 3 (cas limites) : OK")

if __name__ == "__main__":
    test_topKFrequent_basic()
    test_topKFrequent_with_duplicates()
    test

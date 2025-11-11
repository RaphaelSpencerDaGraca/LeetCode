from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())


def test_groupAnagrams_basic():
    sol = Solution()
    input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    expected = [
        ["eat", "tea", "ate"],
        ["tan", "nat"],
        ["bat"]
    ]
    result = sol.groupAnagrams(input_strs)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])
    print("Test 1 (cas classique) : OK")

def test_groupAnagrams_edge_cases():
    sol = Solution()
    input_strs = ["", "", "a", "a", "b"]
    expected = [
        ["", ""],
        ["a", "a"],
        ["b"]
    ]
    result = sol.groupAnagrams(input_strs)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])
    print("Test 2 (mots vides et doublons) : OK")

def test_groupAnagrams_special_chars():
    sol = Solution()
    input_strs = ["eta", "aet", "tan", "nat", "t!a", "a!t"]
    expected = [
        ["eta", "aet"],
        ["tan", "nat"],
        ["t!a", "a!t"]
    ]
    result = sol.groupAnagrams(input_strs)
    assert sorted([sorted(group) for group in result]) == sorted([sorted(group) for group in expected])
    print("Test 3 (caractères spéciaux) : OK")


if __name__ == "__main__":
    try:
        test_groupAnagrams_basic()
        test_groupAnagrams_edge_cases()
        test_groupAnagrams_special_chars()
        print("Tous les tests ont réussi !")
    except AssertionError as e:
        print(f"Un test a échoué : {e}")

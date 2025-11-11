from typing import Dict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) < 1 or len(s) > 50000 or len(t) < 1 or len(t) > 50000 or len(s) != len(t):
            return False
        occurenceS = {}
        occurenceT = {}
        for char in s:
            if char in occurenceS:
                occurenceS[char] += 1
            else:
                occurenceS[char] = 1
        for char in t:
            if char in occurenceT:
                occurenceT[char] += 1
            else:
                occurenceT[char] = 1
        return occurenceS == occurenceT

def test_isAnagram_basic():
    sol = Solution()
    assert sol.isAnagram("anagram", "nagaram") == True
    print("Test 1 (cas classique) : OK")

def test_isAnagram_not_anagram():
    sol = Solution()
    assert sol.isAnagram("rat", "car") == False
    print("Test 2 (pas des anagrammes) : OK")

def test_isAnagram_edge_cases():
    sol = Solution()
    assert sol.isAnagram("a", "a") == True
    assert sol.isAnagram("ab", "aa") == False
    print("Test 3 (cas limites) : OK")

if __name__ == "__main__":
    test_isAnagram_basic()
    test_isAnagram_not_anagram()
    test_isAnagram_edge_cases()

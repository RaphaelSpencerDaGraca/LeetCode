import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_cleaned = re.sub(r"[^a-zA-Z0-9]","",s).lower()
        return str_cleaned == str_cleaned[::-1]
    


def test_validPalindromes():
    sol = Solution()

    assert sol.isPalindrome("A man, a plan, a canal: Panama") == True
    assert sol.isPalindrome("race a car") == True
    assert sol.isPalindrome(" ") == True



if __name__ == "__main__":
    test_validPalindromes()

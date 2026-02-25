class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        for prefix in range(min(len(str1), len(str2)), 0, -1):
            gcd_candidate = str1[:prefix]
            if all(gcd_candidate * (len(s) // prefix) == s for s in (str1, str2)):
                return gcd_candidate
        return ""


# str1 = "ABCABC"
# str2 = "ABC"
str1 = "AAAAAAAAA"
str2 = "AAACCC"

solution = Solution()

print(solution.gcdOfStrings(str1, str2))

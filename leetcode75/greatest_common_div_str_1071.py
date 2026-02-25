class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 == str2:
            return str1

        if len(str1) <= len(str2):
            min_str = str1
            max_str = str2
        else:
            min_str = str2
            max_str = str1

        for prefix in range(len(min_str), 0, -1):
            if len(max_str) % prefix or len(min_str) % prefix:
                continue

            gcd_candidate = min_str[:prefix]
            if all(gcd_candidate * (len(s) // prefix) == s for s in (min_str, max_str)):
                return gcd_candidate
        return ""


# str1 = "ABAB"
# str2 = "ABA"
str1 = "AAAAAAAAA"
str2 = "AAACCC"

solution = Solution()

print(solution.gcdOfStrings(str1, str2))

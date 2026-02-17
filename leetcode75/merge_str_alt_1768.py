from itertools import zip_longest


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if not word1 and not word2:
            return ""

        result = ""
        for char1, char2 in zip_longest(word1, word2, fillvalue=""):
            result += char1 + char2
        return result


solution = Solution()

print(solution.mergeAlternately("hola", "fofo"))

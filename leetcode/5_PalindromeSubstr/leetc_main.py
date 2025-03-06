# Implementing the first leet code solution as practice


class Solution:
    def check_palindrome(self, s: str) -> bool:
        startp, endp = 0, len(s) - 1

        while startp < endp:
            if s[startp] != s[endp]:
                return False
            startp += 1
            endp -= 1
        return True

    def longestPalindrome(self, s: str) -> str:
        for lenght in range(len(s), 0, -1):
            for left in range(len(s) - lenght + 1):
                subword = s[left : left + lenght]
                result = self.check_palindrome(subword)
                if result:
                    return subword
        return ""


def main():
    target = Solution()
    result = target.longestPalindrome("a")
    print(result)


if __name__ == "__main__":
    main()

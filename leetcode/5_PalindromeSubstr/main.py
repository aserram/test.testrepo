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
        startp, endp = 0, len(s) - 1
        str_len = endp
        palind_len = 0
        palidrome = None

        while startp <= (str_len):
            if s[startp] == s[endp]:
                str_to_check = s[startp : endp + 1]
                if len(str_to_check) > palind_len and self.check_palindrome(str_to_check):
                    palidrome = str_to_check
                    palind_len = len(palidrome)

            if startp >= (endp - 1):
                startp += 1
                endp = str_len
            else:
                endp -= 1
        return palidrome


def main():
    target = Solution()
    result = target.longestPalindrome("cbbdddsholaeeadios")
    print(result)


if __name__ == "__main__":
    main()

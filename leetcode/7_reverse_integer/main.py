class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        reversed = 0
        while x != 0:
            x, digit = divmod(x, 10)
            reversed = reversed * 10 + digit
        if reversed > (2**31) - 1:
            return 0
        else:
            return sign * reversed


def main():
    target = Solution()
    result = target.reverse(-1 * 423)
    print(result)


if __name__ == "__main__":
    main()

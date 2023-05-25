class Solution:
    def __init__(self):
        self.roman_table = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str):  # -> int:
        int_value = 0
        prev_roman = s[-1]
        for idx, roman in enumerate(reversed(s)):
            if self.roman_table[roman] >= self.roman_table[prev_roman]:
                int_value += self.roman_table[roman]
            else:
                int_value = int_value - self.roman_table[roman]

            prev_roman = roman
        print(int_value)


def main():
    print("Converting roman numeral to integer value:")

    solution = Solution()
    solution.romanToInt("MCMXCIV")


if __name__ == '__main__':
    main()

class Solution:
    def __init__(self):
        self.roman_table = [
            {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX"},
            {1: "X", 2: "XX", 3: "XXX", 4: "XL", 5: "L", 6: "LX", 7: "LXX", 8: "LXXX", 9: "XC"},
            {1: "C", 2: "CC", 3: "CCC", 4: "CD", 5: "D", 6: "DC", 7: "DCC", 8: "DCCC", 9: "CM"},
            {1: "M", 2: "MM", 3: "MMM"},
        ]

    def intToRoman(self, num: int) -> str:
        roman_num = ""
        decimal = 0
        while num > 0 and num < 4000:
            num, remainder = divmod(num, 10)

            if remainder:
                roman_num = "".join([self.roman_table[decimal][remainder], roman_num])
            decimal += 1
        return roman_num


def main():
    target = Solution()
    roman_num = target.intToRoman(3490)
    print(roman_num)


if __name__ == "__main__":
    main()

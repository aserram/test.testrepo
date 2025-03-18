from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.digit_table = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []

        result = []


def main():
    target = Solution()
    output = target.letterCombinations("23")
    print(output)


if __name__ == "__main__":
    main()

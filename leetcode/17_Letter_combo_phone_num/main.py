from typing import List


class Solution:
    def __init__(self):
        self.result = []
        self.phone_digits = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

    def backtrack(self, digits, idx, comb):
        if idx == len(digits):
            self.result.append(comb)
            return

        for letter in self.phone_digits[digits[idx]]:
            self.backtrack(digits, idx + 1, comb + letter)

    def letterCombinations(self, digits: str) -> List[str]:
        if not len(digits):
            return []
        self.backtrack(digits, 0, "")
        return self.result


def main():
    target = Solution()
    output = target.letterCombinations("4652")
    print(output)


if __name__ == "__main__":
    main()

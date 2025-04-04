from typing import List


class Solution:
    def __init__(self):
        self.results = []

    def backtrack(self, n, combination, idx):
        # placeholder (arguments also)
        if idx == 2 * n - 1:
            self.results.append(combination)
        else:
            pass

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack(n, "", 0)
        return self.results


def main():
    target = Solution()
    result = target.generateParenthesis(2)


if __name__ == "__main__":
    main()

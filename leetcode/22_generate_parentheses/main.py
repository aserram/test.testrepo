from typing import List


class Solution:
    def __init__(self):
        self.results = []

    def backtrack(self, n, combination, open, close):
        if open == close == n:
            self.results.append(combination)

        if open < n:
            self.backtrack(n, combination + "(", open + 1, close)
        if close < open:
            self.backtrack(n, combination + ")", open, close + 1)

    def generateParenthesis(self, n: int) -> List[str]:
        self.backtrack(n, "", 0, 0)
        return self.results


def main():
    target = Solution()
    result = target.generateParenthesis(3)


if __name__ == "__main__":
    main()

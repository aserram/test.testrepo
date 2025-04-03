class Solution:
    def isValid(self, s: str) -> bool:
        bracket_mapping = {"(": ")", "[": "]", "{": "}"}
        opening_stack = []

        if len(s) % 2:
            return False

        for char in s:
            if char in bracket_mapping.keys():
                opening_stack.append(char)
            elif char in bracket_mapping.values():
                if not opening_stack or (opening_stack and bracket_mapping[opening_stack.pop()] != char):
                    return False

        return not opening_stack


def main():
    target = Solution()
    result = target.isValid("))")
    print(result)


if __name__ == "__main__":
    main()

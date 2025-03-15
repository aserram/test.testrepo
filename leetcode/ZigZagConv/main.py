class Solution:
    def convert(self, s: str, numRows: int) -> str:
        main_column = True
        rowidx = 0
        zz_covertion = [""] * numRows
        for char in s:
            zz_covertion[rowidx] += char
            if numRows > 1:
                if main_column:
                    rowidx += 1
                else:
                    rowidx -= 1

            if rowidx == numRows - 1:
                main_column = False
            elif rowidx == 0:
                main_column = True
        return "".join(zz_covertion)


def main():
    target = Solution()
    result_str = target.convert("CULOCONCACA", 3)
    print(result_str)


if __name__ == "__main__":
    main()

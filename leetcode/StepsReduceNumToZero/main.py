
class Solution:
    def numberOfSteps(self, num: int) -> int:
        reduce_to_cero = 0
        while num > 0:
            if num % 2 != 0:
                num = num -1
            else:
                num = num/2
            reduce_to_cero += 1
        return reduce_to_cero

def main():
    target = Solution()
    reduce_to_cero = target.numberOfSteps(123)
    print(reduce_to_cero)

if __name__ == "__main__":
    main()

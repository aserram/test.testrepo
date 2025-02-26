from typing import List


class BinarySearch:
    def find_element(self, array: List[int], target: int) -> float:
        start = 0
        end = len(array) - 1

        while start <= end:
            middle = int((end + start) / 2)
            if array[middle] == target:
                return middle
            elif array[middle] > target:
                end = middle - 1
            elif array[middle] < target:
                start = middle + 1
        return None

def main():
    array = [0, 4, 6, 7, 8, 11, 14, 17, 21, 27, 33, 54, 56] 
    target = BinarySearch()
    result = target.find_element(array, 21)
    if result is not None:
        print(f"The target is in index: {result}")
    else:
        print("The target in not in the array")


if __name__ == "__main__":
    main()

from typing import List
import timeit

class search_algo:
    def binary_search(self, array: List[int], target: int) -> int:
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
    array = list(range(1000000)) 
    target = search_algo()
    
    result = target.binary_search(array, 499999)
    print("*****BINARY SEARCH*****")
    if result is not None:
        print(f"The target is in index: {result}")
    else:
        print("The target in not in the array")

if __name__ == "__main__":
    #main()
    n=3
    result = timeit.timeit(stmt='main()', globals=globals(), number=n)
    print(f"Execution time is {1000*(result/n)}ms")
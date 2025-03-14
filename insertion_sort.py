from typing import List, Dict
def insert_sort(numbers: List[int], ascending: bool = True)-> List[int]:
    """_Sort a list of numbers in given order_

    Args:
        numbers (List[int]): _A list of integers_
        ascending (bool, optional): _Order of sorting_. Defaults to True.

    Returns:
        List[int]: _Sorted list either ascending or descending_
    """
    key: int = 0
    index_to_move = 0
    found = False

    while key < len(numbers):
        number_to_move = numbers[key]

        for index in range(key, len(numbers)):
            if ascending:
                if numbers[index] < number_to_move:
                    number_to_move = numbers[index]
                    index_to_move= index
                    found = True

            else:
                if numbers[index] > number_to_move:
                    number_to_move = numbers[index]
                    index_to_move= index
                    found = True
        if found:
            numbers[key], numbers[index_to_move]=  numbers[index_to_move], numbers[key]
            found = False
            key += 1
        else:
            key += 1

    return numbers
def main() -> None:
    numbers: List[int] = [-5, -9, 7, 8, -4, 1, -2]
    insert_sort(numbers= numbers, ascending = True)
    print(f"Numbers sorted is {numbers}")

if __name__ == "__main__":
    main()
from typing import List, Dict
def insert_sort(numbers: List[int], ascending: bool = True)-> List[int]:
    key: int = 0

    while key < len(numbers):
        smallest = numbers[key]
        smallest_value: Dict[int, int] ={}
        for index in range(key, len(numbers)):
            if numbers[index] < smallest:
                smallest = numbers[index]
                smallest_value['smallest'] = index, smallest
        if 'smallest' in smallest_value:
            smallest_index = smallest_value['smallest'][0]
            smallest_index_value = smallest_value['smallest'][1]
            numbers[key], numbers[smallest_index]=  smallest_index_value, numbers[key]
            key += 1
        else:
            break
    return numbers
def main() -> None:
    numbers: List[int] = [5, 9, 7, 8, 4, 1, 2]
    insert_sort(numbers= numbers)
    print(f"Numbers sorted is {numbers}")

if __name__ == "__main__":
    main()
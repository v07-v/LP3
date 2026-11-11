import random
import time


def deterministic_quick_sort(array, low, high):
    """Sort array[low:high + 1] using a deterministic pivot."""
    if low < high:
        pivot_index = partition(array, low, high)
        deterministic_quick_sort(array, low, pivot_index - 1)
        deterministic_quick_sort(array, pivot_index + 1, high)


def randomized_quick_sort(array, low, high):
    """Sort array[low:high + 1] using a randomized pivot."""
    if low < high:
        pivot_index = randomized_partition(array, low, high)
        randomized_quick_sort(array, low, pivot_index - 1)
        randomized_quick_sort(array, pivot_index + 1, high)


def partition(array, low, high):
    """Partition the array around its last element."""
    pivot_value = array[high]
    smaller_element_index = low - 1

    for current_index in range(low, high):
        if array[current_index] <= pivot_value:
            smaller_element_index += 1
            swap(array, smaller_element_index, current_index)

    swap(array, smaller_element_index + 1, high)
    return smaller_element_index + 1


def randomized_partition(array, low, high):
    """Choose a random pivot and partition the array around it."""
    random_pivot_index = random.randint(low, high)
    swap(array, random_pivot_index, high)
    return partition(array, low, high)


def swap(array, first_index, second_index):
    array[first_index], array[second_index] = (
        array[second_index],
        array[first_index],
    )


def print_array(array):
    print(*array)


def main():
    original_array = list(
        map(int, input("Enter array elements separated by spaces: ").split())
    )

    if not original_array:
        print("Please enter at least one array element.")
        return

    element_count = len(original_array)

    print("Original Array:")
    print_array(original_array)

    deterministic_array = original_array.copy()
    start_time = time.perf_counter_ns()
    deterministic_quick_sort(deterministic_array, 0, element_count - 1)
    end_time = time.perf_counter_ns()

    print("Sorted Array using Deterministic QuickSort:")
    print_array(deterministic_array)
    print(
        "Time taken by Deterministic QuickSort: "
        f"{end_time - start_time} ns"
    )

    randomized_array = original_array.copy()
    start_time = time.perf_counter_ns()
    randomized_quick_sort(randomized_array, 0, element_count - 1)
    end_time = time.perf_counter_ns()

    print("Sorted Array using Randomized QuickSort:")
    print_array(randomized_array)
    print(
        "Time taken by Randomized QuickSort: "
        f"{end_time - start_time} ns"
    )


if __name__ == "__main__":
    main()


# Sample input:
# 10 7 8 9 1 5
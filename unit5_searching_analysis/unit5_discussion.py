"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

This program demonstrates and compares linear search
and binary search using small datasets, large datasets,
and several edge cases.
"""


def linear_search(lst, target):
    """
    Linear Search

    Searches the list from beginning to end.

    Time Complexity: O(n)

    In the worst case, linear search may need to examine
    every element in the list before finding the target
    or determining that it does not exist.
    """

    for index in range(len(lst)):

        # Compare each item to the target value
        if lst[index] == target:
            return index

    # Target not found
    return -1


def binary_search(lst, target):
    """
    Binary Search

    Requires a sorted list.

    Time Complexity: O(log n)

    Binary search repeatedly cuts the search space
    in half, making it much faster than linear search
    for large sorted datasets.
    """

    left = 0
    right = len(lst) - 1

    while left <= right:

        # Find middle position
        mid = (left + right) // 2

        if lst[mid] == target:
            return mid

        # Target must be in the right half
        elif lst[mid] < target:
            left = mid + 1

        # Target must be in the left half
        else:
            right = mid - 1

    # Target not found
    return -1


def main():

    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ==================================================
    # SMALL DATASET
    # ==================================================

    print("\n=== SMALL DATASET TEST ===")

    small_dataset = [10, 20, 30, 40, 50]

    print("Dataset:", small_dataset)

    existing_value = 30
    missing_value = 35

    print("\nSearching for existing value:", existing_value)

    print(
        "Linear Search Index:",
        linear_search(small_dataset, existing_value)
    )

    print(
        "Binary Search Index:",
        binary_search(small_dataset, existing_value)
    )

    print("\nSearching for missing value:", missing_value)

    print(
        "Linear Search Index:",
        linear_search(small_dataset, missing_value)
    )

    print(
        "Binary Search Index:",
        binary_search(small_dataset, missing_value)
    )

    # ==================================================
    # LARGE DATASET
    # ==================================================

    print("\n=== LARGE DATASET TEST ===")

    large_dataset = list(range(1, 10001))

    target = 9876

    print("Large Dataset Size:", len(large_dataset))
    print("Target Value:", target)

    print(
        "Linear Search Index:",
        linear_search(large_dataset, target)
    )

    print(
        "Binary Search Index:",
        binary_search(large_dataset, target)
    )

    print(
        "\nBinary search is more efficient because it "
        "eliminates half of the remaining data each iteration."
    )

    # ==================================================
    # EDGE CASES
    # ==================================================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty List
    empty_list = []

    print("\nEdge Case 1 - Empty List")

    print(
        "Linear Search:",
        linear_search(empty_list, 10)
    )

    print(
        "Binary Search:",
        binary_search(empty_list, 10)
    )

    # Edge Case 2: Single Element
    single_element = [25]

    print("\nEdge Case 2 - Single Element List")

    print(
        "Linear Search:",
        linear_search(single_element, 25)
    )

    print(
        "Binary Search:",
        binary_search(single_element, 25)
    )

    # Edge Case 3: First Element
    print("\nEdge Case 3 - First Element")

    print(
        "Linear Search:",
        linear_search(small_dataset, 10)
    )

    print(
        "Binary Search:",
        binary_search(small_dataset, 10)
    )

    # Edge Case 4: Last Element
    print("\nEdge Case 4 - Last Element")

    print(
        "Linear Search:",
        linear_search(small_dataset, 50)
    )

    print(
        "Binary Search:",
        binary_search(small_dataset, 50)
    )

    # Edge Case 5: Value Not Present
    print("\nEdge Case 5 - Value Not Present")

    print(
        "Linear Search:",
        linear_search(small_dataset, 99)
    )

    print(
        "Binary Search:",
        binary_search(small_dataset, 99)
    )

    print("\nProgram Complete.")


if __name__ == "__main__":
    main()
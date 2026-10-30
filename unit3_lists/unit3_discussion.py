"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

This program demonstrates insertion, deletion, and searching
operations using Python lists.
"""


def insert_at(lst, index, value):
    """
    Inserts a value into the list at the specified index.
    """

    # Elements at and after the insertion point shift right
    # to make room for the new value.
    # Insertions near the beginning require more shifting.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Removes and returns the value at the specified index.
    Returns None if the index is invalid.
    """

    # Validate the index before deleting.
    if index < 0 or index >= len(lst):
        return None

    # Elements shift left after removal.
    return lst.pop(index)


def search_value(lst, value):
    """
    Searches for a value in the list.

    Returns the index if found.
    Returns -1 if not found.
    """

    # Linear search checks each element one at a time.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    print("\n=== INSERTION TESTS ===")

    # Real-world example: playlist management
    playlist = ["Song A", "Song B", "Song C"]

    print("Original Playlist:", playlist)

    insert_at(playlist, 0, "Intro Song")
    print("After inserting at beginning:", playlist)

    insert_at(playlist, 2, "Middle Song")
    print("After inserting in middle:", playlist)

    insert_at(playlist, len(playlist), "Final Song")
    print("After inserting at end:", playlist)

    print("\n=== DELETION TESTS ===")

    removed = delete_at(playlist, 0)
    print("Removed from beginning:", removed)
    print("Updated Playlist:", playlist)

    removed = delete_at(playlist, 2)
    print("Removed from middle:", removed)
    print("Updated Playlist:", playlist)

    removed = delete_at(playlist, len(playlist) - 1)
    print("Removed from end:", removed)
    print("Updated Playlist:", playlist)

    print("\n=== SEARCH TESTS ===")

    result = search_value(playlist, "Song C")
    print("Search for existing value 'Song C':", result)

    result = search_value(playlist, "Unknown Song")
    print("Search for missing value 'Unknown Song':", result)

    print("\n=== EDGE CASES ===")

    result = delete_at(playlist, 100)
    print("Delete using invalid index:", result)

    empty_list = []
    insert_at(empty_list, 0, "First Item")
    print("Insert into empty list:", empty_list)

    empty_list = []
    result = delete_at(empty_list, 0)
    print("Delete from empty list:", result)

    result = search_value(["A", "B", "C"], "Z")
    print("Search for missing value:", result)


if __name__ == "__main__":
    main()
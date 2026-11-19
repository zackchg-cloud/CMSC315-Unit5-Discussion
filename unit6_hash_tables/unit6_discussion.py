"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================
"""

def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================

    print("\n=== INSERT OPERATIONS ===")

    # Python dictionaries function as hash tables.
    # Keys are hashed to determine where values are stored.
    # This provides very fast average-case lookup performance.

    inventory = {}

    inventory["L100"] = "Laptop"
    inventory["P200"] = "Printer"
    inventory["M300"] = "Monitor"
    inventory["K400"] = "Keyboard"
    inventory["T500"] = "Tablet"

    print("Inventory:")
    print(inventory)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # Lookup uses the key's hash value to quickly locate data.
    print("L100:", inventory["L100"])
    print("P200:", inventory["P200"])

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:")
    print(inventory)

    # Assigning a new value to an existing key updates that entry.
    inventory["L100"] = "Gaming Laptop"

    print("After update:")
    print(inventory)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("Before delete:")
    print(inventory)

    # Removing a key deletes its associated value.
    del inventory["K400"]

    print("After delete:")
    print(inventory)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Lookup a missing key safely
    print("Missing key lookup:")
    print(inventory.get("X999", "Equipment not found"))

    # Edge Case 2: Safe deletion
    removed = inventory.pop("X999", None)

    if removed is None:
        print("Attempted delete of missing key handled safely.")

    # Edge Case 3: Empty dictionary
    empty_inventory = {}

    print("Empty dictionary:")
    print(empty_inventory)


if __name__ == "__main__":
    main()
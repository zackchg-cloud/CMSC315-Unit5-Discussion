"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

The program demonstrates recursive insertion, searching,
and in-order traversal operations.
"""


class Node:
    def __init__(self, value):
        # Store the node's value and initialize references
        # to the left and right child nodes.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Values smaller than the current node go into the
        left subtree, while larger values go into the
        right subtree. This organization helps make
        searches more efficient.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.

        Creates a new node when an empty position
        is found and returns the updated node.
        """

        if node is None:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

        # Duplicate values are ignored.
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        BST search is efficient because each comparison
        eliminates part of the remaining search space.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """

        if node is None:
            return False

        if node.value == value:
            return True

        if value < node.value:
            return self._search_recursive(node.left, value)

        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """

        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.

        In-order traversal visits:
        1. Left subtree
        2. Current node
        3. Right subtree

        Because BST values are ordered from smaller
        to larger values, an in-order traversal
        produces sorted output.
        """

        if node is not None:
            self._inorder_recursive(node.left, values)
            values.append(node.value)
            self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================
    #
    # Employee IDs are used as a
    # real-world BST example.
    #
    # A BST reduces search space because
    # each comparison determines whether
    # to search left or right.

    print("\n=== TREE CONSTRUCTION ===")

    tree = BST()

    employee_ids = [50, 25, 75, 10, 30, 60, 90]

    for emp_id in employee_ids:
        tree.insert(emp_id)

    print("Employee IDs inserted:")
    print(employee_ids)

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================

    print("\n=== IN-ORDER TRAVERSAL ===")

    traversal = tree.inorder()

    print("In-order traversal:")
    print(traversal)

    # The output is sorted because
    # in-order traversal visits
    # left subtree, node, and right subtree.

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    print("Search for 50:", tree.search(50))
    print("Search for 90:", tree.search(90))

    print("Search for 45:", tree.search(45))
    print("Search for 100:", tree.search(100))

    # True indicates a value was found.
    # False indicates the value does not
    # exist in the tree.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    empty_tree = BST()

    print("Search empty tree for 15:", empty_tree.search(15))
    print("Traverse empty tree:", empty_tree.inorder())

    tree.insert(50)

    print("Traversal after attempting duplicate insert (50):")
    print(tree.inorder())

    # Duplicate values are ignored and
    # therefore do not change the tree.


if __name__ == "__main__":
    main()
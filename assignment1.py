class Node:
    """Class representing a single node in a linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """Class to manage the singly linked list."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Add a node with the given data to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            print(f"Appended '{data}' as head.")
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            print(f"Appended '{data}' to the end.")

    def print_list(self):
        """Print all nodes in the list."""
        if self.head is None:
            print("List is empty.")
            return
        current = self.head
        print("Linked List:", end=" ")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_nth_node(self, n):
        """Delete the nth node (1-based index) from the list."""
        try:
            if self.head is None:
                raise IndexError("Cannot delete from an empty list.")

            if n <= 0:
                raise IndexError("Index must be a positive integer.")

            # Deleting the head node
            if n == 1:
                print(f"Deleting node at position {n} with value '{self.head.data}'")
                self.head = self.head.next
                return

            # Traverse to the node before the one to be deleted
            current = self.head
            count = 1
            while current is not None and count < n - 1:
                current = current.next
                count += 1

            if current is None or current.next is None:
                raise IndexError("Index out of range.")

            print(f"Deleting node at position {n} with value '{current.next.data}'")
            current.next = current.next.next

        except IndexError as e:
            print("Error:", e)


# Testing the implementation
if __name__ == "__main__":
    ll = LinkedList()

    # Add nodes
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.append(40)

    # Print list
    ll.print_list()

    # Delete node at position 2
    ll.delete_nth_node(2)
    ll.print_list()

    # Delete node at invalid position
    ll.delete_nth_node(10)

    # Delete all remaining nodes
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)
    ll.delete_nth_node(1)

    # Try deleting from empty list
    ll.delete_nth_node(1)

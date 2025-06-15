# Singly Linked List in Python (OOP Implementation)

This project demonstrates a basic implementation of a **Singly Linked List** using **Object-Oriented Programming (OOP)** principles in Python.

## 📌 Features

- Object-oriented design with `Node` and `LinkedList` classes
- Add a node to the **end** of the list
- **Print** the entire linked list
- **Delete** the nth node (1-based index)
- **Exception handling** for:
  - Deleting from an empty list
  - Invalid index (e.g., out of range, zero, or negative)

## 🛠️ Classes and Methods

### `Node`
Represents each node in the list.
- `data`: stores the node's value
- `next`: points to the next node

### `LinkedList`
Manages the linked list.
- `append(data)`: Adds a new node to the end
- `print_list()`: Prints the current state of the list
- `delete_nth_node(n)`: Deletes the node at the nth position

## ✅ Example Usage

```python
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.print_list()           # Output: 10 -> 20 -> 30 -> None
ll.delete_nth_node(2)     # Deletes node with value 20
ll.print_list()           # Output: 10 -> 30 -> None

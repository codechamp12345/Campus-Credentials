from __future__ import print_function


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def addNode(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node


    def addNodeBeginning(self, value):
        node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node


    def addNodeInBetween(self, pos, value):
        if pos <= 0:
            print("Invalid position!")
            return
        node = Node(value)
        current = self.head
        count = 1
        while current is not None and count < pos - 1:
            current = current.next
            count += 1
        if current is None:
            print("Position out of range.")
        else:
            node.next = current.next
            current.next = node
            if node.next is None:
                self.tail = node


    def addNodeEnd(self, value):
        self.addNode(value) # Already implemented in addNode


    def displayNode(self):
        current = self.head
        while current is not None:
            print(current.data, '|', current.next, '->', end=" ")
            current = current.next
        print("None")


if __name__ == '__main__':
    object = LinkedList()


    while True:
        print("\n1. Add Node Linkedlist (End)")
        print("2. Add Node in Beginning")
        print("3. Add Node in Between")
        print("4. Add Node in End")
        print("5. Display Linkedlist")
        print("6. Exit")


        try:
            ch = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid integer choice!")
            continue


        if ch == 1:
            value = int(input("Enter the value: "))
            object.addNode(value)
            print("Node added successfully at the end!")


        elif ch == 2:
            value = int(input("Enter the value: "))
            object.addNodeBeginning(value)
            print("Node added at the beginning successfully!")


        elif ch == 3:
            value = int(input("Enter the value: "))
            pos = int(input("Enter the position (starting from 1): "))
            object.addNodeInBetween(pos, value)
            print("Node added in between successfully!")


        elif ch == 4:
            value = int(input("Enter the value: "))
            object.addNodeEnd(value)
            print("Node added at the end successfully!")


        elif ch == 5:
            object.displayNode()


        elif ch == 6:
            print("Exiting...")
            break


        else:
            print("Invalid choice! Please try again.")

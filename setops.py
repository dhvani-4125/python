class SetDemo:

    def __init__(self):
        n = int(input("Enter number of elements: "))
        self.my_set = set()

        for i in range(n):
            value = input(f"Enter element {i + 1}: ")
            self.my_set.add(value)

    def display(self):
        return self.my_set

    def add_element(self):
        value = input("Enter element to add: ")
        self.my_set.add(value)
        return self.my_set

    def remove_element(self):
        value = input("Enter element to remove: ")
        self.my_set.remove(value)
        return self.my_set

    def discard_element(self):
        value = input("Enter element to discard: ")
        self.my_set.discard(value)
        return self.my_set

    def pop_element(self):
        self.my_set.pop()
        return self.my_set

    def clear_set(self):
        self.my_set.clear()
        return self.my_set

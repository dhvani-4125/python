class ListDemo:

    def __init__(self):
        n = int(input("Enter number of elements in the list: "))
        self.my_list = []

        for i in range(n):
            value = input(f"Enter element {i + 1}: ")
            self.my_list.append(value)

    def display(self):
        return self.my_list

    def append_element(self):
        value = input("Enter element to append: ")
        self.my_list.append(value)
        return self.my_list

    def insert_element(self):
        index = int(input("Enter index: "))
        value = input("Enter value: ")
        self.my_list.insert(index, value)
        return self.my_list

    def remove_element(self):
        value = input("Enter element to remove: ")
        self.my_list.remove(value)
        return self.my_list

    def pop_element(self):
        self.my_list.pop()
        return self.my_list

    def reverse_list(self):
        self.my_list.reverse()
        return self.my_list

    def sort_list(self):
        self.my_list.sort()
        return self.my_list

    def count_element(self):
        value = input("Enter value to count: ")
        return self.my_list.count(value)

    def index_element(self):
        value = input("Enter value to find index: ")
        return self.my_list.index(value)

    def length(self):
        return len(self.my_list)

    def clear_list(self):
        self.my_list.clear()
        return self.my_list

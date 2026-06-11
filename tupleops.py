class TupleDemo:

    def __init__(self):
        n = int(input("Enter number of tuple elements: "))

        temp = []

        for i in range(n):
            value = input(f"Enter element {i + 1}: ")
            temp.append(value)

        self.my_tuple = tuple(temp)

    def display(self):
        print(self.my_tuple)

    def count_element(self):
        value = input("Enter value to count: ")
        print(self.my_tuple.count(value))

    def index_element(self):
        value = input("Enter value to find index: ")
        print(self.my_tuple.index(value))

    def length(self):
        print(len(self.my_tuple))

    def maximum(self):
        print(max(self.my_tuple))

    def minimum(self):
        print(min(self.my_tuple))

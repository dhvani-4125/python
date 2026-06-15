class DictDemo:

    def __init__(self):
        n = int(input("Enter number of key-value pairs: "))
        self.my_dict = {}

        for i in range(n):
            key = input("Enter key: ")
            value = input("Enter value: ")
            self.my_dict[key] = value

    def display(self):
        return self.my_dict

    def keys_method(self):
        return self.my_dict.keys()

    def values_method(self):
        return self.my_dict.values()

    def items_method(self):
        return self.my_dict.items()

    def get_value(self):
        key = input("Enter key: ")
        return self.my_dict.get(key)

    def update_value(self):
        key = input("Enter key to update: ")
        value = input("Enter new value: ")
        self.my_dict[key] = value
        return self.my_dict

    def pop_item(self):
        key = input("Enter key to pop: ")
        self.my_dict.pop(key)
        return self.my_dict

    def pop_last(self):
        self.my_dict.popitem()
        return self.my_dict

    def clear_dict(self):
        self.my_dict.clear()
        return self.my_dict

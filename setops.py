class SetDemo:

    def create_set(self):
        self.my_set = {10, 20, 30}
        print("Set:", self.my_set)

    def add_element(self):
        self.my_set.add(40)
        print("After adding:", self.my_set)

    def remove_element(self):
        self.my_set.remove(20)
        print("After removing:", self.my_set)
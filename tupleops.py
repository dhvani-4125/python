class ListDemo:

    def create_list(self):
        self.my_list = [10, 20, 30, 40]
        print("List:", self.my_list)

    def add_element(self):
        self.my_list.append(50)
        print("After adding:", self.my_list)

    def remove_element(self):
        self.my_list.remove(20)
        print("After removing:", self.my_list)
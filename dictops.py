class DictDemo:

    def create_dict(self):
        self.my_dict = {
            "name": "Dhvani",
            "age": 20
        }
        print("Dictionary:", self.my_dict)

    def add_item(self):
        self.my_dict["city"] = "Surat"
        print("After adding:", self.my_dict)

    def display_keys(self):
        print("Keys:", self.my_dict.keys())
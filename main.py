from listops import ListDemo
from tupleops import TupleDemo
from dictops import DictDemo
from setops import SetDemo

# List object
list_obj = ListDemo()
list_obj.create_list()
list_obj.add_element()
list_obj.remove_element()

print()

# Tuple object
tuple_obj = TupleDemo()
tuple_obj.create_tuple()
tuple_obj.length()
tuple_obj.access_element()

print()

# Dictionary object
dict_obj = DictDemo()
dict_obj.create_dict()
dict_obj.add_item()
dict_obj.display_keys()

print()

# Set object
set_obj = SetDemo()
set_obj.create_set()
set_obj.add_element()
set_obj.remove_element()
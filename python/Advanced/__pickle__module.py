"""
:return: Pickle module helps to store the data in the form of
         Binary format of data in the extension of .pkl...

         pickle.dump(): Helps to dump the data into the form
         of binary mode.

         pickle.load(): Helps to read the pickle file from the
         binary mode file. .pkl
"""

import pickle

__cars_list = ["Audio", "Harryti Suzuki", "Ferrari", "BMW-I8"]
_car_list_file = "__cars_list.pkl"
_cars_list_obj = open(_car_list_file, "wb")
pickle.dump(__cars_list, _cars_list_obj)
_cars_list_obj.close()

# Read the pickle module file
__read__pickle = open(_car_list_file, "rb")
print(pickle.load(__read__pickle))
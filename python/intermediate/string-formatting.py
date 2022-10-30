"""
   F strings works as a template literal in python
"""
import math

me = "Andy"
age = "16"


def old_variable_string_formatting():
    variable = "Mink"
    print("This is %s" % variable)


def double_Tuple_string_Formatting():
    """
       :return: Not readable
    """
    me = "Andy"
    age = "16"
    output = "The tuple variable %s %s" % (me, age)
    print(output)


def format_string_formatting():
    format_set = "Values are {} {}"
    output_format_set = format_set.format(me, age)
    print(output_format_set)


format_string_formatting()


""" 
   F strings 
   
"""
f_strings = f"Value of factorial is {math.factorial(5)}"
print(f_strings)
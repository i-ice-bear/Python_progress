"""
:return: Regex, and regular expression, is a function in python
         which performs a search pattern in the program,
         it's used to find a search character in the string and
         any other data or not.
"""


import re as regex

normal__string = "Aya, ima motherfucker"
search_abusive = regex.search("^Aya,.*motherfucker$", normal__string)
print(f"Aya, men i founded {search_abusive}")

txt = "The rain in Spain"
x = regex.search("^The.*Spain$", txt)
print(x)
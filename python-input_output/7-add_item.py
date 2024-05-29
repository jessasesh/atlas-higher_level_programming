#!/usr/bin/python3
"""
Script that adds all arguments to a Python list,
and then save them to a file.
"""
import os
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

my_list = []

if os.path.exists("add_item.json"):
    my_list = load_from_json_file("add_item.json")
else:
    my_list = []
for x in range(1, len(argv)):
    my_list.append(argv[x])
save_to_json_file(my_list, "add_item.json")

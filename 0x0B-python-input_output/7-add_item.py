#!/usr/bin/python3
"""Script to all arguments to a list and save them to a file"""


from sys import argv
save_to_json = __import__('5-save_to_json_file').save_to_json_file
load_from_json = __import__('6-load_from_json_file').load_from_json_file
filename = "add_item.json"
arg_list = load_from_json(filename)
arg_list.extend(argv[1:])
save_to_json(arg_list, filename)

#!/usr/bin/python3
"""
7-add_item.py
"""

import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

try:
    lis = load_from_json_file("add_item.json")
except Exception:
    lis = []

for i in range(1, len(sys.argv)):
    lis.append(sys.argv[i])

save_to_json_file(lis, "add_item.json")

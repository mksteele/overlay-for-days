import os

from file_paths import *

def read_items_from_src(src):
    with open(os.path.join('resources', src), 'r') as f:
        items = [x.strip() for x in f.readlines()]
        items.sort()
        return items

def read_team_names():
    return read_items_from_src(TEAM_NAMES_FILE)

def write_file(fname, value):
    print("Writing '{}' to {}".format(value, fname))

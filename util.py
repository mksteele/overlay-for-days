import os

from shutil import copyfile
from file_paths import *


def read_items_from_src(src):
    with open(os.path.join('resources', src), 'r') as f:
        items = [x.strip() for x in f.readlines()]
        items.sort()
        return items

def read_teams():
    return read_items_from_src(TEAM_NAMES_FILE)

def remove_team(team):
    teams = read_teams()
    teams.remove(team)
    print("New teams: {}".format(teams))
    with open(os.path.join('resources', TEAM_NAMES_FILE), 'w') as f:
        [ f.write("{}\n".format(x)) for x in teams ]

def write_file(fname, value):
    print("Writing '{}' to {}".format(value, fname))
    with open(os.path.join('resources', fname), 'w') as f:
        f.write(value)

def replace_team_names_with_original():
    """ Used only for testing """
    copyfile(os.path.join('resources', GOLDEN_TEAM_NAMES_FILE),
            os.path.join('resources', TEAM_NAMES_FILE))

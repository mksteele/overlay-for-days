import os

from shutil import copyfile
from file_paths import *


def read_file(src):
    """ Returns a list if the file has multiple lines, else one value """
    with open(os.path.join('resources', src), 'r') as f:
        items = [x.strip() for x in f.readlines()]
        if len(items) > 1:
            return sorted(items, key=lambda s: s.lower())
        else:
            return items[0] if items else ""

def read_teams():
    return read_file(TEAM_NAMES_FILE)

def write_teams(teams):
    print("New teams: {}".format(teams))
    write_file(TEAM_NAMES_FILE, teams)

def add_team_to_file(team):
    teams = read_teams() + [team]
    teams = sorted(teams, key=lambda s: s.lower())
    write_teams(teams)

def remove_team_from_file(team):
    teams = read_teams()
    teams.remove(team)
    print("New teams: {}".format(teams))
    write_teams(teams)

def write_file(fname, value_or_values):
    print("Writing '{}' to {}".format(value_or_values, fname))
    with open(os.path.join('resources', fname), 'w') as f:
        if isinstance(value_or_values, list):
            [ f.write("{}\n".format(x)) for x in value_or_values]
        else:
            f.write(value_or_values)

def replace_team_names_with_original():
    """ Used only for testing """
    copyfile(os.path.join('resources', GOLDEN_TEAM_NAMES_FILE),
            os.path.join('resources', TEAM_NAMES_FILE))

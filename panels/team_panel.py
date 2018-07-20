import ttk

from Tkinter import *

from util import *

"""
Team Panel
 - Shows existing teams
 - Allows you to 
"""

WIDTH = 200
HEIGHT = 100

class TeamPanel:

    def __init__(self, parent):
        # Setup
        self.parent = parent

        self.create_team_names()

    def create_team_names(self):
        row = 0
        teams = read_team_names()
        for team in teams:
            team_label = Label(self.parent, text=team)
            team_label.grid(row=row, column=0, sticky="ew")
            row = row + 1


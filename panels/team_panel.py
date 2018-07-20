from Tkinter import Label, Entry

from util import read_team_names
from base_panel import BasePanel

"""
TeamPanel
 - Shows existing teams
 - Allows you to add and remove teams
"""

class TeamPanel(BasePanel):

    def __init__(self, parent):
        # Setup
        BasePanel.__init__(self, parent, 'Teams')

        self.create_team_names()

    def create_team_names(self):
        row = 0
        teams = read_team_names()
        for team in teams:
            team_label = Label(self.content, text=team)
            team_label.grid(row=row, column=0, sticky="ew")
            row = row + 1


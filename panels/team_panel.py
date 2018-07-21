from Tkinter import *

from util import read_teams, remove_team
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

        self.create_teams()
        self.create_add_team_entry()

    def create_teams(self):
        row = 0
        teams = read_teams()
        for team in teams:
            team_label = Label(self.content, text=team)
            team_label.grid(row=row, column=0) #, sticky="ew")

            def rem_team(t=team):
                remove_team(t)
                self.clear()
                self.create_teams()

            x_button = Button(self.content, text='x',
                    command=rem_team)
            x_button.grid(row=row, column=1)
            row = row + 1

        # Going to pass bottom row to 
        return row

    def create_add_team_entry(self):
        """ Want a text entry where we can add a new team """
        add_team_str = StringVar(self.content)
        add_team_str.set(" ") # To make the cursor show up
        add_team_entry = Entry(self.content, textvariable=add_team_str)
        add_team_entry.grid(row=0, column=0, sticky=S)
        #add_team_entry.grid_rowconfigure(0, weight=1)


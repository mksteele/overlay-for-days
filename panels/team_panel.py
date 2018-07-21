import ttk

from Tkinter import *

from util import read_teams, remove_team
from base_panel import BasePanel

from lib.vertical_scrolled_frame import VerticalScrolledFrame

"""
TeamPanel
 - Shows existing teams
 - Allows you to add and remove teams
"""

TEAM_HEIGHT = 10

class TeamPanel(BasePanel):

    def __init__(self, parent):
        # Setup
        BasePanel.__init__(self, parent, 'Teams')

        self.content.configure(bg='red')

        self.create_teams()
        self.create_add_team_entry()

    def create_teams(self):
        team_list_frame = Frame(self.content)
        team_list_frame.grid(row=0, column=0)

        teams = read_teams()

        if len(teams) > TEAM_HEIGHT:
            scrollbar = Scrollbar(team_list_frame)
            scrollbar.pack(side=RIGHT, fill=Y)
            listbox = Listbox(team_list_frame, yscrollcommand=scrollbar.set)
        else:
            listbox = Listbox(team_list_frame)

        def rem_team(t):
            remove_team(t)
            team_list.destroy()
            self.create_teams()

        for team in teams:
            listbox.insert(END, team)
        listbox.pack(side=LEFT, fill=BOTH)

    def create_add_team_entry(self):
        """ Want a text entry where we can add a new team """
        add_team_str = StringVar(self.content)
        add_team_str.set(" ") # To make the cursor show up
        add_team_entry = Entry(self.content, textvariable=add_team_str)
        add_team_entry.grid(row=1, column=0)
        #add_team_entry.grid_rowconfigure(0, weight=1)


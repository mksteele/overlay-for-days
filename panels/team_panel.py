import ttk

from Tkinter import *

from util import read_teams, add_team_to_file, remove_team_from_file
from base_panel import BasePanel

from lib.vertical_scrolled_frame import VerticalScrolledFrame

"""
TeamPanel
 - Shows existing teams
 - Allows you to add and remove teams
"""

TEAM_HEIGHT = 10

class TeamPanel(BasePanel):

    def __init__(self, parent, notify_callback):
        # Setup
        BasePanel.__init__(self, parent, 'Teams')

        self.notify_callback = notify_callback

        self.content.configure(bg='red')

        self.create_teams()
        self.create_add_team_entry()

    def create_teams(self):
        self.team_list_frame = Frame(self.content)
        self.team_list_frame.grid(row=0, column=0)

        teams = read_teams()

        self.listbox = Listbox(self.team_list_frame, height=TEAM_HEIGHT,
                borderwidth=0, highlightthickness=0)
        scrollbar = Scrollbar(self.team_list_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        self.populate_listbox()
        self.listbox.pack(side=LEFT, fill=BOTH)

        def rem_team(event):
            selection = self.listbox.curselection()
            if selection:
                remove_team_from_file(self.listbox.get(selection[0]))
                self.listbox.delete(selection[0])
                self.notify_callback()
        self.listbox.bind('<BackSpace>', rem_team)
        self.listbox.bind('<Delete>', rem_team)

    def populate_listbox(self):
        teams = read_teams()
        for team in teams:
            self.listbox.insert(END, team)

    def create_add_team_entry(self):
        """ Want a text entry where we can add a new team """
        add_team_str = StringVar(self.content)
        add_team_entry = Entry(self.content, textvariable=add_team_str)
        add_team_entry.grid(row=1, column=0)

        def add_team_to_listbox(*args):
            new_team = add_team_str.get().strip()
            if new_team:
                add_team_to_file(new_team)
                add_team_str.set("")
                self.listbox.delete(0, 'end')
                self.populate_listbox()

        plus_button = Button(self.content, command=add_team_to_listbox, text='+')
        plus_button.grid(row=1, column=1)
        add_team_entry.bind('<Return>', add_team_to_listbox)


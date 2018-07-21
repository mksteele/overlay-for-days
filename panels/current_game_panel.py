import Tkinter as tk

from Tkinter import *

from base_panel import BasePanel
from file_paths import TEAM_NAME_PATTERN
from util import read_file, read_teams, write_file

COLORS = [ "Blue", "Gold" ]

def team_fname(color):
    return TEAM_NAME_PATTERN.format(Color=color)

class CurrentGamePanel(BasePanel):

    def __init__(self, parent):
        BasePanel.__init__(self, parent, 'Current Game')

        self.create_team_selectors()
        self.create_swap_button()

    def create_team_selectors(self):
        """ Make dropdown menus for selecting teams """
        self.team_selectors = {}
        teams = read_teams()

        row = 0
        for color in COLORS:
            label = Label(self.content, text="{} Team:".format(color))
            label.grid(row=row, column=0, sticky="ew")

            str_var = StringVar(self.content)
            prev_team_from_file = read_file(team_fname(color))
            str_var.set(prev_team_from_file)
            def make_on_change(color=color, str_var=str_var):
                def on_change(*args):
                    write_file(team_fname(color), str_var.get())
                return on_change

            str_var.trace("w", make_on_change())
            selector = OptionMenu(self.content, str_var, *teams)
            selector.grid(row=row, column=1, sticky="ew")
            row = row + 1
            # Store everything
            self.team_selectors[color] = {}
            self.team_selectors[color]["obj"] = selector
            self.team_selectors[color]["str_var"] = str_var 

    def notify_teams_change(self):
        """ Change the menu options when the team list changes """
        new_teams = read_teams()
        for color in COLORS:
            # Reset var and delete all old options
            str_var = self.team_selectors[color]["str_var"]

            # We had previously selected a deleted team. Let's set
            # that to nothing
            if str_var.get() not in new_teams:
                str_var.set("")
            selector = self.team_selectors[color]["obj"]
            selector['menu'].delete(0, 'end')

            # Insert list of new options (tk._setit hooks them up to var)
            for team in new_teams:
                selector['menu'].add_command(label=team,
                        command=tk._setit(str_var, team))

    def create_swap_button(self):
        """ Make a button to swap blue and gold teams. """
        swap_button = Button(self.content, text="Swap Teams")
        swap_button.grid(row=3, column=1)

        def swap_team():
            """ Do the team swapping"""
            blue_team_str = self.team_selectors["Blue"]["str_var"]
            gold_team_str = self.team_selectors["Gold"]["str_var"]

            tmp = gold_team_str.get()
            gold_team_str.set(blue_team_str.get())
            blue_team_str.set(tmp)

        swap_button.configure(command=swap_team)

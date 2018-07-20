import ttk

from Tkinter import *

from base_panel import BasePanel
from util import read_team_names, write_file

layout = {
    "labels": {
        "Blue score:": { "row": 0, "col": 0 },
        "Gold score:": { "row": 1, "col": 0 },
        "Blue team:": { "row": 2, "col": 0 },
        "Gold team:": { "row": 3, "col": 0 },
    },
    "text_entries": {
        "blue score": { "row": 0, "col": 1, "out": "Gold Score.txt" },
        "gold score": { "row": 1, "col": 1, "out": "Blue Score.txt" },
    },
    "dropdowns": {
        "blue team": { "row": 2, "col": 1, "out": "Blue Team Name.txt"},
        "gold team": { "row": 3, "col": 1, "out": "Gold Team Name.txt"},
    },
    "buttons": {
        "Swap Teams" : { "row": 4, "col": 0 },
    },
}

class CurrentGamePanel(BasePanel):

    def __init__(self, parent):
        BasePanel.__init__(self, parent, 'Current Game')

        self.create_buttons()
        self.create_labels()
        self.create_text_entries()
        self.create_dropdowns()

        self.make_swap_team_button_swap_team()
        self.grid_everything()

    def create_buttons(self):
        # For each type of thing, create the object that we want
        for text, info in layout["buttons"].iteritems():
            info["obj"] = Button(self.content, text=text)

    def create_labels(self):
        for text, info in layout["labels"].iteritems():
            info["obj"] = Label(self.content, text=text)

    def create_text_entries(self):
        for _, info in layout["text_entries"].iteritems():
            info["string_var"] = StringVar(self.content)
            info["string_var"].set(" ") # To make the cursor show up
            info["obj"] = Entry(self.content, textvariable=info["string_var"], justify=RIGHT)

    def create_dropdowns(self):
        """ Not going to create drop downs in a generic way """

        teams = read_team_names()
        blue_info = layout["dropdowns"]["blue team"]
        blue_info["string_var"] = StringVar(self.content)
        if len(teams) > 0:
            blue_info["string_var"].set(teams[0]) # default value

        def write_blue_file(*args):
            new_value = blue_info["string_var"].get().strip()
            write_file(blue_info["out"], new_value)

        # Call write_blue_file every time this variable changes 
        blue_info["string_var"].trace("w", write_blue_file)
        blue_info["obj"] = OptionMenu(self.content, blue_info["string_var"], *teams)

        gold_info = layout["dropdowns"]["gold team"]
        gold_info["string_var"] = StringVar(self.content)
        if len(teams) > 1:
            gold_info["string_var"].set(teams[1]) # default value

        def write_gold_file(*args):
            new_value = gold_info["string_var"].get().strip()
            write_file(gold_info["out"], new_value)

        # Call write_gold_file every time this variable changes 
        gold_info["string_var"].trace("w", write_gold_file)
        gold_info["obj"] = OptionMenu(self.content, gold_info["string_var"], *teams)

    def grid_everything(self):
        """ Actually place the widgets in the grid """
        for k, v in layout.iteritems():
            for _, info in v.iteritems():
                info["obj"].grid(row=info["row"], column=info["col"], sticky="ew")

    def make_swap_team_button_swap_team(self):
        """ Swap blue and gold teams. """
        swap_team_button = layout["buttons"]["Swap Teams"]["obj"]

        def swap_team():
            """ Do the team swapping"""
            gold_team_str = layout["dropdowns"]["gold team"]["string_var"]
            blue_team_str = layout["dropdowns"]["blue team"]["string_var"]

            tmp = gold_team_str.get()
            gold_team_str.set(blue_team_str.get())
            blue_team_str.set(tmp)

        swap_team_button.configure(command=swap_team)

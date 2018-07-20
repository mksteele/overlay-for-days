import os
import ttk

from Tkinter import *

""" 
TODO:
    - do I even care about scores?
    - idea for a miscellaneous ticker area:
            Labels that you can drag and drop
            Entry at the bottom to add things to the ticker, with a plus sign
            X buttons next to the ticker items 
"""



WIDTH = 200
HEIGHT = 100

NUM_COL = 4
NUM_ROW = 5

TEAM_NAMES_FILE = "team_names.txt"

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
        "Swap Teams" : { "row": NUM_ROW-1, "col": 0 },
    },
}

def read_items_from_src(src):
    with open(os.path.join('resources', src), 'r') as f:
        items = [x.strip() for x in f.readlines()]
        items.sort()
        return items

def read_team_names():
    return read_items_from_src(TEAM_NAMES_FILE)

class OverlayForDays:

    def __init__(self, root):
        # Setup
        #self.content = Frame(root)
        self.content = ttk.Labelframe(root, text='Current Game')
        self.content.grid(column=1, row=0, padx=10, pady=10)

        self.team_panel = ttk.Labelframe(root, text='Teams')
        self.team_panel.grid(column=0, row=0, padx=10, pady=10)
        background = Frame(self.team_panel, width=WIDTH, height=HEIGHT)
        background.grid(column=0, row=0, columnspan=NUM_COL, rowspan=NUM_ROW)

        self.create_buttons()
        self.create_labels()
        self.create_text_entries()
        self.create_dropdowns()

        self.make_swap_team_button_swap_team()

        self.create_team_names()
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
            print("Writing '{}' to {}".format(new_value, blue_info["out"]))

        # Call write_blue_file every time this variable changes 
        blue_info["string_var"].trace("w", write_blue_file)
        blue_info["obj"] = OptionMenu(self.content, blue_info["string_var"], *teams)

        gold_info = layout["dropdowns"]["gold team"]
        gold_info["string_var"] = StringVar(self.content)
        if len(teams) > 1:
            gold_info["string_var"].set(teams[1]) # default value

        def write_gold_file(*args):
            new_value = gold_info["string_var"].get().strip()
            print("Writing '{}' to {}".format(new_value, gold_info["out"]))

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

    def create_team_names(self):
        row = 0
        teams = read_team_names()
        for team in teams:
            team_label = Label(self.team_panel, text=team)
            team_label.grid(row=row, column=0, sticky="ew")
            row = row + 1


def main():
    root = Tk()
    root.title("Overlay for days")
    app = OverlayForDays(root)
    root.mainloop()

if __name__ == "__main__":
    main()

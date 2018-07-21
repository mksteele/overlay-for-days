from Tkinter import Tk

from panels import *
from util import replace_team_names_with_original

class OverlayForDays:

    def __init__(self, root):
        self.team_panel = TeamPanel(root, self.notify_teams_change)
        self.team_panel.grid(column=0, row=0, padx=10, pady=10)

        self.current_game_panel = CurrentGamePanel(root)
        self.current_game_panel.grid(column=1, row=0, padx=10, pady=10)

        self.ticker_panel = TickerPanel(root)
        self.ticker_panel.grid(row=1, columnspan=2, padx=10, pady=10)

    def notify_teams_change(self):
        # Notify all panels that the teams list has changed
        self.current_game_panel.notify_teams_change()

def main():
    root = Tk()
    root.title("Overlay for days")

    # TODO remove
    replace_team_names_with_original()

    app = OverlayForDays(root)
    root.mainloop()

if __name__ == "__main__":
    main()

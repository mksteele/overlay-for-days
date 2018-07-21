from Tkinter import Tk

from panels import *
from util import replace_files_with_originals

WIDTH = 300
HEIGHT = 250

class OverlayForDays:

    def __init__(self, root):
        padx = 10
        pady = 10
        team_panel_width = 250
        current_game_panel_width = 380
        ticker_panel_width = team_panel_width + current_game_panel_width + 2*padx

        self.team_panel = TeamPanel(root, self.notify_teams_change,
                width=team_panel_width, height=HEIGHT)
        self.team_panel.grid(column=0, row=0, padx=10, pady=10)

        self.current_game_panel = CurrentGamePanel(root,
                width=current_game_panel_width,
                height=HEIGHT)
        self.current_game_panel.grid(column=1, row=0, padx=10, pady=10)

        self.ticker_panel = TickerPanel(root, width=ticker_panel_width, height=230)
        self.ticker_panel.grid(row=1, columnspan=2, padx=10, pady=10)

    def notify_teams_change(self):
        # Notify all panels that the teams list has changed
        self.current_game_panel.notify_teams_change()

def main():
    root = Tk()
    root.title("Overlay for days")

    # TODO remove
    replace_files_with_originals()

    app = OverlayForDays(root)
    root.mainloop()

if __name__ == "__main__":
    main()

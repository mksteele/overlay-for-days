from Tkinter import Tk

from panels import *

class OverlayForDays:

    def __init__(self, root):
        #self.current_game_panel = CurrentGamePanel()
        #self.current_game_panel.grid(column=1, row=0, padx=10, pady=10)

        self.team_panel = TeamPanel()
        self.team_panel.grid(column=0, row=0, padx=10, pady=10)

def main():
    root = Tk()
    root.title("Overlay for days")
    app = OverlayForDays(root)
    root.mainloop()

if __name__ == "__main__":
    main()

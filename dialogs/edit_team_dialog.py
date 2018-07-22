from Tkinter import *

from lib.tkSimpleDialog import Dialog

class EditTeamDialog(Dialog):

    def __init__(self, parent, team_info, title="Edit Team"):
        """
        Expect team_info to be in format:
        [ "Team name", "Player1", "Player2", "Player3", "Player4", "Player5" ]
        """
        self.team_info = team_info
        Dialog.__init__(self, parent, title=title)

    def body(self, master):
        Label(master, text="Team name:").grid(row=0)
        for i in range(1, 6):
            Label(master, text="Player {}:".format(i)).grid(row=i)

        self.entries = []
        for i in range(0, 6):
            self.entries.append(Entry(master))
            self.entries[i].grid(row=i, column=1)

            if self.team_info and len(self.team_info) > i:
                self.entries[i].insert(0, self.team_info[i])

        self.error = Label(master, fg='red')
        self.error.grid(row=i+1, columnspan=2)
        return self.entries[0] # initial focus

    def apply(self):
        self.result = [self.entries[i].get().strip() for i in range(0, 6)]
        print "Result: {}".format(self.result)

    def validate(self):
        any_player_populated = False
        for i in range(1, 6):
            if self.entries[i].get():
                any_player_populated = True
        if not self.entries[0].get() and any_player_populated:
            self.error.configure(text="Error: Team name cannot be blank.")
            return 0
        return 1


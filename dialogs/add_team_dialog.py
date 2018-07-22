from edit_team_dialog import EditTeamDialog

class AddTeamDialog(EditTeamDialog):

    def __init__(self, parent):
        EditTeamDialog.__init__(self, parent, None, title="Add Team")

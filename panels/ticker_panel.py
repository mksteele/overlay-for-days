from Tkinter import *

from base_panel import BasePanel
#from util import read_teams, add_team_to_file, remove_team_from_file
from lib.drag_drop_listbox import DragDropListbox

class TickerPanel(BasePanel):

    def __init__(self, parent):
        # Setup
        BasePanel.__init__(self, parent, 'Ticker', width=640, height=230)


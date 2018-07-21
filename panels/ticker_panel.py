from Tkinter import *

from base_panel import BasePanel
from lib.drag_drop_listbox import DragDropListbox
from util import read_ticker

class TickerPanel(BasePanel):

    def __init__(self, parent, width=None, height=None):
        # Setup
        BasePanel.__init__(self, parent, 'Ticker', width=width,
                height=height)

        self.create_tickers()
        self.create_add_ticker_entry()

    def create_tickers(self):
        self.ticker_list_frame = Frame(self.content, bg='blue',
                width=self.content.winfo_width())
        self.ticker_list_frame.grid(row=0, column=0)

        self.listbox = DragDropListbox(self.ticker_list_frame,
                borderwidth=0, highlightthickness=0)
        scrollbar = Scrollbar(self.ticker_list_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        self.populate_listbox()
        self.listbox.pack(side=LEFT, fill=BOTH)

        def rem_ticker(event):
            selection = self.listbox.curselection()
            if selection:
                remove_ticker_from_file(self.listbox.get(selection[0]))
                self.listbox.delete(selection[0])
                self.notify_callback()
        self.listbox.bind('<BackSpace>', rem_ticker)
        self.listbox.bind('<Delete>', rem_ticker)

    def populate_listbox(self):
        #tickers = read_tickers()
        # TODO: read from file
        tickers = read_ticker()
        for ticker in tickers:
            self.listbox.insert(END, ticker)

    def create_add_ticker_entry(self):
        """ Want a text entry where we can add a new ticker """
        add_ticker_str = StringVar(self.content)
        add_ticker_entry = Entry(self.content, textvariable=add_ticker_str)
        add_ticker_entry.grid(row=1, column=0)

        def add_ticker_to_listbox(*args):
            new_ticker = add_ticker_str.get().strip()
            if new_ticker:
                #add_ticker_to_file(new_ticker)
                add_ticker_str.set("")
                self.listbox.delete(0, 'end')
                self.populate_listbox()

        plus_button = Button(self.content, command=add_ticker_to_listbox, text='+')
        plus_button.grid(row=1, column=1)
        add_ticker_entry.bind('<Return>', add_ticker_to_listbox)

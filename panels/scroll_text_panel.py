from Tkinter import *

from base_panel import BasePanel
from lib.drag_drop_listbox import DragDropListbox
from util import read_scroll_text

class ScrollTextPanel(BasePanel):

    def __init__(self, parent, width=None, height=None):
        # Setup
        BasePanel.__init__(self, parent, 'Scroll Text', width=width,
                height=height)

        #self.create_scroll_texts()

    def create_scroll_texts(self):
        self.scroll_text_list_frame = Frame(self.content)
        self.scroll_text_list_frame.grid(row=0, column=0)

        self.listbox = DragDropListbox(self.scroll_text_list_frame,
                borderwidth=0, highlightthickness=0, width=60)
        scrollbar = Scrollbar(self.scroll_text_list_frame)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        self.populate_listbox()
        self.listbox.pack(side=LEFT, fill=BOTH)

        def rem_scroll_text(event):
            selection = self.listbox.curselection()
            if selection:
                remove_scroll_text_from_file(self.listbox.get(selection[0]))
                self.listbox.delete(selection[0])
                self.notify_callback()
        self.listbox.bind('<BackSpace>', rem_scroll_text)
        self.listbox.bind('<Delete>', rem_scroll_text)
        self.create_add_scroll_text_entry()

    def populate_listbox(self):
        #scroll_texts = read_scroll_texts()
        # TODO: read from file
        scroll_texts = read_scroll_text()
        for scroll_text in scroll_texts:
            self.listbox.insert(END, scroll_text)

    def create_add_scroll_text_entry(self):
        """ Want a text entry where we can add a new scroll_text """
        add_scroll_text_str = StringVar(self.content)
        add_scroll_text_entry = Entry(self.content, textvariable=add_scroll_text_str)
        add_scroll_text_entry.grid(row=1, column=0)

        def add_scroll_text_to_listbox(*args):
            new_scroll_text = add_scroll_text_str.get().strip()
            if new_scroll_text:
                #add_scroll_text_to_file(new_scroll_text)
                add_scroll_text_str.set("")
                self.listbox.delete(0, 'end')
                self.populate_listbox()

        plus_button = Button(self.content, command=add_scroll_text_to_listbox, text='+')
        plus_button.grid(row=1, column=1)
        add_scroll_text_entry.bind('<Return>', add_scroll_text_to_listbox)

from tkinter import *

class Application(Frame):
  def __init__(self, parent=None):
    Frame.__init__(self, parent)
    self.pack()
    self.create_widgets()
    parent.bind('<Key>', self.key)
    self.entry.focus_set()
    self.lbox.select_set(0)
    self.sel_index = 0          # index of selected item

  def create_widgets(self):
    self.search_var = StringVar()
    self.search_var.trace('w', self.update_list)
    self.entry = Entry(self, textvariable=self.search_var, width=13)
    self.lbox = Listbox(self, width=45, height=15, selectmode=SINGLE)
    self.entry.grid(row=0, column=0, padx=10, pady=3)
    self.lbox.grid(row=1, column=0, padx=10, pady=3)
    self.update_list()

  def update_list(self, n=None, m=None, k=None):
    search_term = self.search_var.get()
    lbox_list = ['Adam','Lucy','Barry','Bob','James','Frank','Susan','Amanda','Christie']
    self.num_lbox_items = len(lbox_list)
    self.lbox.delete(0, END)
    for item in lbox_list:
      if search_term.lower() in item.lower():
        self.lbox.insert(END, item)

  def key(self, event):
    if event.keysym == 'Up':
      self.lbox.selection_clear(0, END)     # clear any selected items
      self.sel_index -= 1
      if self.sel_index < 0:
          self.sel_index = 0
      self.lbox.select_set(self.sel_index)
    if event.keysym == 'Down':
      self.lbox.selection_clear(0, END)     # clear any selected items
      self.sel_index += 1
      if self.sel_index >= self.num_lbox_items:
          self.sel_index = self.num_lbox_items - 1
      self.lbox.select_set(self.sel_index)
    if event.keysym == 'Return':
      print(self.lbox.curselection())
    print(self.lbox.curselection())

root = Tk()
app = Application(parent=root)
app.mainloop()

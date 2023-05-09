import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import asksaveasfilename, askopenfilename


class Notepad:
    def __init__(self, master):
        self.master = master
        self.master.title("PyPad 1.0")
        self.textarea = tk.Text(self.master, undo=True)
        self.textarea.pack(fill='both', expand=True)
        self.menubar = tk.Menu(self.master)
        self.master.config(menu=self.menubar)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='New', command=self.new_file)
        self.filemenu.add_command(label='Open', command=self.open_file)
        self.filemenu.add_command(label='Save', command=self.save_file)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit', command=self.master.quit)

    def new_file(self):
        self.textarea.delete('1.0', 'end')

    def open_file(self):
        filepath = askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        self.textarea.delete('1.0', 'end')
        with open(filepath, 'r') as file:
            self.textarea.insert('1.0', file.read())

    def save_file(self):
        filepath = asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if not filepath:
            return
        with open(filepath, 'w') as file:
            file.write(self.textarea.get('1.0', 'end'))

if __name__ == '__main__':
    root = tk.Tk()
    Notepad(root)
    root.mainloop()

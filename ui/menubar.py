import tkinter as tk


class Menubar(tk.Menu):
    
    app = None
    
    def __init__(self, app):
        super().__init__(app)
        self.app = app
        self.init_ui()
        
    def init_ui(self):
        filemenu = tk.Menu(self, tearoff=0)
        filemenu.add_command(label="New", command=self.new_callback, accelerator="Ctrl+N")
        filemenu.add_command(label="Load", command=self.load_callback, accelerator="Ctrl+L")
        filemenu.add_command(label="Save", command=self.save_callback, accelerator="Ctrl+S")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.exit_callback, accelerator="Ctrl+Q")
        self.add_cascade(label="File", menu=filemenu)

        editmenu = tk.Menu(self, tearoff=0)
        editmenu.add_command(label="Undo", command=self.undo_callback, accelerator="Ctrl+Z")
        editmenu.add_command(label="Redo", command=self.redo_callback, accelerator="Ctrl+Y")
        self.add_cascade(label="Edit", menu=editmenu)

        helpmenu = tk.Menu(self, tearoff=0)
        helpmenu.add_command(label="Help Index", command=self.help_callback)
        helpmenu.add_command(label="About...", command=self.about_callback)
        self.add_cascade(label="Help", menu=helpmenu)
    
    def new_callback(self):
        self.app.on_new_ui(None)
        
    def load_callback(self):
        self.app.on_load_ui(None)
        
    def save_callback(self):
        self.app.on_save_ui(None)
        
    def exit_callback(self):
        self.app.on_exit(None)
        
    def help_callback(self):
        return
        
    def about_callback(self):
        return
        
    def undo_callback(self):
        self.app.on_undo(None)
        
    def redo_callback(self):
        self.app.on_redo(None)

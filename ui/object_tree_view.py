import tkinter as tk
from tkinter import ttk

class ObjectTreeView(tk.LabelFrame):
    
    tree = None
    scrollbar = None
    selected_object = None
    item_uid_pairs = {}
    
    def __init__(self, master=None, app=None):
        super().__init__(master, text='Tree')
        self.app = app
        self.init_ui()
        self.init_logic()

    def init_ui(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.tree = ttk.Treeview(self)
        self.tree.grid(row=0, column=0, sticky='news')
        
        self.vscrollbar = tk.Scrollbar(self)
        self.vscrollbar.grid(row=0, column=1, sticky='news')

        self.hscrollbar = tk.Scrollbar(self, orient=tk.HORIZONTAL)
        self.hscrollbar.grid(row=1, column=0, columnspan=2, sticky='news')
        
        self.tree.config(yscrollcommand=self.vscrollbar.set)
        self.tree.config(xscrollcommand=self.hscrollbar.set)
        self.vscrollbar.config(command=self.tree.yview)
        self.hscrollbar.config(command=self.tree.xview)

    def init_logic(self):
        self.tree.bind('<<TreeviewSelect>>', self.on_tree_select)

    def ui_updated(self):
        # fill tree
        self.tree.delete(*self.tree.get_children())
        self.item_uid_pairs.clear()
        current_ui_tree = self.app.get_current_ui_tree()
        
        container_list = []
        for uid in current_ui_tree.keys():
            if current_ui_tree[uid].is_container():
                container_list.append(uid)
        
        item_counter = 0
        container_iid = 0
        for uid in container_list:
            container_string = '#' + uid + ': ' + current_ui_tree[uid].get_node_type() + '.' + current_ui_tree[uid].get_node_name()
            self.tree.insert('', tk.END, text=container_string, iid=item_counter, open=True)
            container_iid = item_counter

            self.item_uid_pairs[item_counter] = uid
            item_counter += 1
            
            children_list = current_ui_tree[uid].get_children()
            child_index = 0
            for child_uid in children_list:
                child_string = '#' + child_uid + ': ' + current_ui_tree[child_uid].get_node_type() + '.' + current_ui_tree[child_uid].get_node_name()
                self.tree.insert('', tk.END, text=child_string, iid=item_counter, open=False)
                self.tree.move(item_counter, container_iid, child_index)
                
                self.item_uid_pairs[item_counter] = child_uid
                item_counter += 1
                child_index += 1
        
        #self.tree.selection_set(0)

    def on_tree_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            self.app.on_object_click(self.item_uid_pairs[int(item)])
        

            

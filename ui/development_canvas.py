import tkinter as tk
import tkinter.ttk as ttk

from app.objects_data import *

class DevelopmentCanvas(tk.LabelFrame):

    app = None
    drawn_objects = None
    hovered_object_uid = None
    highlighted_object_bg = None
    highlighted_object_uid = None
    selected_object_uid = None
    
    def __init__(self, master=None, app=None):
        super().__init__(master, text='Development Canvas')
        self.app = app

    def on_object_hover(self, event):
        self.hovered_object_uid = self.get_uid_of_object(event.widget)[0]
        if self.hovered_object_uid != self.highlighted_object_uid:
            self.remove_object_highlight()
        
            if self.app.get_current_ui_tree()[self.hovered_object_uid].is_container():
                self.highlighted_object_uid = self.hovered_object_uid
                self.highlighted_object_bg = event.widget['background']
                event.widget.configure(bg='red')

    def on_object_leave(self, event):
        self.remove_object_highlight()

    def remove_object_highlight(self):
        if self.highlighted_object_uid != None:
            self.drawn_objects[self.highlighted_object_uid].configure(bg=self.highlighted_object_bg)
            self.highlighted_object_uid = None
            self.highlighted_object_bg = None

    def on_object_click(self, event):
        obj_uid = self.get_uid_of_object(event.widget)[0]
        self.app.on_object_click(obj_uid)

    def on_object_selected(self, uid):
        self.selected_object_uid = uid

    def ui_updated(self):
        self.draw_objects()

    def clear_objects(self):
        if self.drawn_objects is not None:
            if self.drawn_objects['0'] is not None:
                self.drawn_objects['0'].destroy()
            self.drawn_objects.clear()

    def draw_objects(self):
        self.clear_objects()
        self.drawn_objects = {}
        for uid, node in self.app.get_current_ui_tree().items():
            self.draw_object(node)

    def draw_object(self, node):
        parent_node = None
        new_obj = None
        node_attributes_list = None
        parent_attributes_list = None

        node_attributes_list = node.get_attributes_list()
        parent_node = node.get_parent()
        parent_obj = self if parent_node == None else self.drawn_objects[parent_node]
        if parent_node is not None:
            parent_attributes_list = self.app.get_current_ui_tree()[node.get_parent()].get_attributes_list()

        if 'Frame' == node.node_type:
            new_obj = self.draw_frame(node, node_attributes_list, parent_obj, parent_attributes_list)
        
        elif 'Canvas' == node.node_type:
            new_obj = self.draw_canvas(node, node_attributes_list, parent_obj, parent_attributes_list)
            
        elif 'LabelFrame' == node.node_type:
            new_obj = self.draw_labelframe(node, node_attributes_list, parent_obj, parent_attributes_list)
            
        elif 'Button' == node.node_type:
            new_obj = self.draw_button(node, node_attributes_list, parent_obj, parent_attributes_list)
            
        elif 'Checkbutton' == node.node_type:
            new_obj = self.draw_checkbutton(node, node_attributes_list, parent_obj, parent_attributes_list)
            
        elif 'Entry' == node.node_type:
            new_obj = self.draw_entry(node, node_attributes_list, parent_obj, parent_attributes_list)
            
        elif 'Label' == node.node_type:
            new_obj = self.draw_label(node, node_attributes_list, parent_obj, parent_attributes_list)
        
        elif 'Listbox' == node.node_type:
            new_obj = self.draw_listbox(node, node_attributes_list, parent_obj, parent_attributes_list)
        
        elif 'Radiobutton' == node.node_type:
            new_obj = self.draw_radiobutton(node, node_attributes_list, parent_obj, parent_attributes_list)
        
        elif 'Scrollbar' == node.node_type:
            new_obj = self.draw_scrollbar(node, node_attributes_list, parent_obj, parent_attributes_list)

        elif 'Text' == node.node_type:
            new_obj = self.draw_text(node, node_attributes_list, parent_obj, parent_attributes_list)
        
        elif 'Spinbox' == node.node_type:
            new_obj = self.draw_spinbox(node, node_attributes_list, parent_obj, parent_attributes_list)
        
        elif 'Combobox' == node.node_type:
            new_obj = self.draw_combobox(node, node_attributes_list, parent_obj, parent_attributes_list)
        
        elif 'Notebook' == node.node_type:
            new_obj = self.draw_notebook(node, node_attributes_list, parent_obj, parent_attributes_list)

        elif 'Progressbar' == node.node_type:
            new_obj = self.draw_progressbar(node, node_attributes_list, parent_obj, parent_attributes_list)

        elif 'Separator' == node.node_type:
            new_obj = self.draw_separator(node, node_attributes_list, parent_obj, parent_attributes_list)

        elif 'Sizegrip' == node.node_type:
            new_obj = self.draw_sizegrip(node, node_attributes_list, parent_obj, parent_attributes_list)

        elif 'Treeview' == node.node_type:
            new_obj = self.draw_treeview(node, node_attributes_list, parent_obj, parent_attributes_list)

        if node.is_container():
            if node_attributes_list[ATTR_INDEX_LAYOUT]['parameters']['type']['value'] == 'grid':
                # column
                column_weights_str_list = node_attributes_list[ATTR_INDEX_LAYOUT]['parameters']['cweights']['value'].split(',')
                column_weights_list = [int(x) for x in  column_weights_str_list]
                for index, val in enumerate(column_weights_list):
                    new_obj.columnconfigure(index, weight=val, uniform='x')
                # row
                row_weights_str_list = node_attributes_list[ATTR_INDEX_LAYOUT]['parameters']['rweights']['value'].split(',')
                row_weights_list = [int(x) for x in row_weights_str_list]
                for index, val in enumerate(row_weights_list):
                    new_obj.rowconfigure(index, weight=val, uniform='x')
        
        padx_val = int(node_attributes_list[ATTR_INDEX_PLACE]['parameters']['padx']['value'])
        pady_val = int(node_attributes_list[ATTR_INDEX_PLACE]['parameters']['pady']['value'])
        ipadx_val = int(node_attributes_list[ATTR_INDEX_PLACE]['parameters']['ipadx']['value'])
        ipady_val = int(node_attributes_list[ATTR_INDEX_PLACE]['parameters']['ipady']['value'])
        
        if parent_attributes_list is not None:
            if 'grid' == parent_attributes_list[ATTR_INDEX_LAYOUT]['parameters']['type']['value']:
                row_val = int(node_attributes_list[ATTR_INDEX_GRID]['parameters']['row']['value'])
                column_val = int(node_attributes_list[ATTR_INDEX_GRID]['parameters']['column']['value'])
                sticky_val = node_attributes_list[ATTR_INDEX_GRID]['parameters']['sticky']['value']

                new_obj.grid(row=row_val, column=column_val, sticky=sticky_val, padx=padx_val, pady=pady_val, ipadx=ipadx_val, ipady=ipady_val)
            else:
                side_val = node_attributes_list[ATTR_INDEX_PACK]['parameters']['side']['value']
                fill_val = node_attributes_list[ATTR_INDEX_PACK]['parameters']['fill']['value']
                expand_val = int(node_attributes_list[ATTR_INDEX_PACK]['parameters']['expand']['value'])

                new_obj.pack(side=side_val, fill=fill_val, expand=expand_val, padx=padx_val, pady=pady_val, ipadx=ipadx_val, ipady=ipady_val)
        else:
            new_obj.pack(side=tk.LEFT, fill=tk.BOTH, expand=1, padx=10, pady=10, ipadx=10, ipady=10)

        self.drawn_objects[node.uid] = new_obj
        new_obj.bind('<Motion>', self.on_object_hover)
        new_obj.bind('<Leave>', self.on_object_leave)
        new_obj.bind('<ButtonRelease-1>', self.on_object_click)

    def draw_frame(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = tk.Frame(parent_obj)
        return new_obj

    def draw_canvas(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = tk.Canvas(parent_obj)
        return new_obj

    def draw_labelframe(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        text_val = node_attributes_list[ATTR_INDEX_SPEC]['parameters']['text']['value']
        new_obj = tk.LabelFrame(parent_obj, text=text_val)
        return new_obj

    def draw_button(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        text_val = node_attributes_list[ATTR_INDEX_SPEC]['parameters']['text']['value']
        new_obj = tk.Button(parent_obj, text=text_val)
        return new_obj

    def draw_checkbutton(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        text_val = node_attributes_list[ATTR_INDEX_SPEC]['parameters']['text']['value']
        new_obj = tk.Checkbutton(parent_obj, text=text_val)
        return new_obj

    def draw_entry(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        show_val = node_attributes_list[ATTR_INDEX_SPEC]['parameters']['show']['value']
        new_obj = tk.Entry(parent_obj, show=show_val)
        return new_obj

    def draw_label(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        text_val = node_attributes_list[ATTR_INDEX_SPEC]['parameters']['text']['value']
        new_obj = tk.Label(parent_obj, text=text_val)
        return new_obj

    def draw_listbox(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = tk.Listbox(parent_obj)
        return new_obj

    def draw_radiobutton(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        text_val = node_attributes_list[ATTR_INDEX_SPEC]['parameters']['text']['value']
        new_obj = tk.Radiobutton(parent_obj, text=text_val)
        return new_obj

    def draw_scrollbar(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        orient_val = node_attributes_list[ATTR_INDEX_SPEC]['parameters']['orient']['value']
        new_obj = tk.Scrollbar(parent_obj, orient=orient_val)
        return new_obj

    def draw_spinbox(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = tk.Spinbox(parent_obj)
        return new_obj

    def draw_text(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = tk.Text(parent_obj)
        return new_obj
    
    def draw_combobox(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = ttk.Combobox(parent_obj)
        return new_obj

    def draw_spinbox(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = ttk.Spinbox(parent_obj)
        return new_obj
    
    def draw_notebook(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = ttk.Notebook(parent_obj)
        return new_obj
    
    def draw_progressbar(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = ttk.Progressbar(parent_obj)
        return new_obj

    def draw_separator(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = ttk.Separator(parent_obj)
        return new_obj
    
    def draw_sizegrip(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = ttk.Sizegrip(parent_obj)
        return new_obj

    def draw_treeview(self, node, node_attributes_list, parent_obj, parent_attributes_list):
        new_obj = ttk.Treeview(parent_obj)
        return new_obj

    def get_uid_of_object(self, node):
        return [k for k, o in self.drawn_objects.items() if o == node]

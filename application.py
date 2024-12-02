import tkinter as tk
import tkinter.filedialog as fd
import tkinter.messagebox as mb
import time
import os

from ui.menubar import Menubar
from ui.place_object_selector import PlaceObjectSelector
from ui.object_tree_view import ObjectTreeView
from ui.development_canvas import DevelopmentCanvas
from ui.attribute_editor import AttributeEditor
import ui.ui_generics as ui

from app.ui_tree import UITree
from app.objects_data import OBJECTS_DATA
from app.ui_class_generator import UIClassGenerator


class Application(tk.Tk):

    # widgets
    console = None

    # appflow
    main_frame = None
    menubar = None
    place_object_selector = None
    object_tree_view = None
    development_canvas = None
    attribute_editor = None
    current_ui_tree = None
    has_unsaved_changes = False

    def __init__(self, geometry):
        super().__init__()
        self.geometry(geometry)
        self.init_logic()
        self.init_ui()
        self.console.write_info('Application init complete.')

    def init_logic(self):
        self.current_ui_tree = UITree(self)
        self.has_unsaved_changes = False
        self.bind('<Control-n>', self.on_new_ui)
        self.bind('<Control-s>', self.on_save_ui)
        self.bind('<Control-l>', self.on_load_ui)
        self.bind('<Control-g>', self.on_generate_code)
        self.bind('<Control-q>', self.on_exit)
        self.bind('<Control-z>', self.on_undo)
        self.bind('<Control-y>', self.on_redo)
        self.bind('<Control-Shift-Z>', self.on_redo)  # Alternative redo shortcut
        self.protocol("WM_DELETE_WINDOW", lambda: self.on_exit(None))

    def init_ui(self):
        self.last_configure_time = time.time()
        self.title('TKGenerator')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.menubar = Menubar(self)
        self.config(menu=self.menubar)

        self.main_frame = tk.Frame(self)
        self.main_frame.grid(row=0, column=0, sticky='news')
        self.main_frame.rowconfigure(0, weight=1)
        self.main_frame.columnconfigure(0, weight=3, uniform="x")
        self.main_frame.columnconfigure(1, weight=5, uniform="x")
        self.main_frame.columnconfigure(2, weight=24, uniform="x")
        self.main_frame.columnconfigure(3, weight=5, uniform="x")

        # console
        self.console = ui.SingleLineConsole(self)
        self.console.grid(column=0, row=1, sticky='news')

        # place frame
        self.place_object_selector = PlaceObjectSelector(self.main_frame, self)
        self.place_object_selector.grid(column=0, row=0, sticky='news')

        # tree frame
        self.object_tree_view = ObjectTreeView(self.main_frame, self)
        self.object_tree_view.grid(row=0, column=1, sticky='news')

        # canvas frame
        self.development_canvas = DevelopmentCanvas(self.main_frame, self)
        self.development_canvas.grid(row=0, column=2, sticky='news')
        self.development_canvas.rowconfigure(0, weight=1)
        self.development_canvas.columnconfigure(0, weight=1)

        # attribute frame
        self.attribute_editor = AttributeEditor(self.main_frame, self)
        self.attribute_editor.rowconfigure(0, weight=1)
        self.attribute_editor.columnconfigure(0, weight=1)
        self.attribute_editor.grid(row=0, column=3, sticky='news')

        self.console.write_info('UI init done.')

        self.ui_updated()

    def mark_unsaved_changes(self):
        """Mark that there are unsaved changes and update the window title"""
        if not self.has_unsaved_changes:
            self.has_unsaved_changes = True
            self.title('TKGenerator *')

    def clear_unsaved_changes(self):
        """Clear the unsaved changes flag and update the window title"""
        if self.has_unsaved_changes:
            self.has_unsaved_changes = False
            self.title('TKGenerator')

    def check_unsaved_changes(self):
        """Check if there are unsaved changes and prompt user if necessary"""
        if self.has_unsaved_changes:
            return mb.askyesno('Unsaved Changes', 'There are unsaved changes. Do you want to continue?')
        return True

    def ui_updated(self):
        """Update UI components and handle undo/redo state"""
        # First update the development canvas to reflect the current UI state
        self.development_canvas.ui_updated()
        
        # Then update the object tree view
        self.object_tree_view.ui_updated()
        
        # Update undo/redo state
        can_undo = self.current_ui_tree.can_undo()
        can_redo = self.current_ui_tree.can_redo()
        
        # Get the Edit menu
        for child in self.menubar.winfo_children():
            if isinstance(child, tk.Menu) and child.entrycget(0, 'label') == 'Edit':
                edit_menu = child
                break
        else:
            return  # Edit menu not found
            
        # Update menu items and their accelerators
        edit_menu.entryconfig("Undo", state="normal" if can_undo else "disabled")
        edit_menu.entryconfig("Redo", state="normal" if can_redo else "disabled")
        
        # Mark unsaved changes
        self.mark_unsaved_changes()
        
        # Force an update of the UI
        self.update_idletasks()

    def on_object_click(self, node_uid):
        # decide what to do
        if self.place_object_selector.selected_object is not None:
            # try to place new object
            node_type_to_place = self.place_object_selector.selected_object
            new_node_uid = self.current_ui_tree.add_node(node_type_to_place, node_uid)
            self.place_object_selector.clear_selected_object()

            if new_node_uid is not None:
                self.ui_updated()
                self.console.write_info('Placed ' + node_type_to_place + '#' + str(new_node_uid) + ' into #' + node_uid + '.')
            else:
                self.console.write_error('Cannot place new object into a non container object.')
        else:
            # select an object from canvas
            self.development_canvas.on_object_selected(node_uid)
            self.attribute_editor.on_object_selected(node_uid)
            self.console.write_info('Selected object #' + node_uid + '.')

    def get_objects_data(self):
        return OBJECTS_DATA

    def get_object_attributes(self, node_uid):
        return self.current_ui_tree.get_node_attributes(node_uid)

    def set_object_attributes(self, node_uid, attributes):
        self.current_ui_tree.set_node_attributes(node_uid, attributes)
        self.ui_updated()
        self.console.write_info('Set object attributes #' + node_uid + '.')

    def get_object_attributes_list(self, object_type):
        return OBJECTS_DATA[object_type]['attributes_list']

    def on_delete_object_click(self, node_uid):
        if node_uid == '0':
            self.console.write_error('Root object not removable.')
        else:
            self.current_ui_tree.remove_node(node_uid)
            self.ui_updated()
            self.console.write_info('Removed object #' + node_uid + '.')

    def get_current_ui_tree(self):
        return self.current_ui_tree.get_all_nodes()

    def on_exit(self, event):
        if self.check_unsaved_changes():
            self.quit()

    def on_new_ui(self, event):
        """Create a new UI, clearing undo/redo history"""
        if self.check_unsaved_changes():
            self.current_ui_tree = UITree(self)
            self.ui_updated()
            self.clear_unsaved_changes()
            self.console.write_info('Created new UI')

    def on_save_ui(self, event):
        try:
            file = fd.asksaveasfile(
                title='Save UI as',
                mode='w',
                initialfile='Untitled.tkui',
                defaultextension=".tkui",
                filetypes=[('TKGen File','*.tkui')]
            )
            if file:
                file.write(self.current_ui_tree.serialize())
                self.clear_unsaved_changes()
                self.console.write_info('Saved UI to ' + file.name + '.')
                file.close()
        except Exception as e:
            mb.showerror('Error', f'Failed to save file: {str(e)}')
            self.console.write_error(f'Failed to save UI: {str(e)}')

    def on_load_ui(self, event):
        if not self.check_unsaved_changes():
            return
            
        try:
            file = fd.askopenfile(
                title='Load UI From File',
                filetypes=[("TKGen File","*.tkui")]
            )
            if file:
                ui_data = file.read()
                ret = self.current_ui_tree.deserialize(ui_data)
                if ret:
                    self.ui_updated()
                    self.clear_unsaved_changes()
                    self.console.write_info('Loaded UI from ' + file.name + '.')
                else:
                    raise ValueError('Invalid UI file format')
                file.close()
        except Exception as e:
            mb.showerror('Error', f'Failed to load file: {str(e)}')
            self.console.write_error(f'Failed to load UI: {str(e)}')
                
    def on_generate_code(self, event):
        try:
            file = fd.asksaveasfile(
                title='Generate class as',
                mode='w',
                initialfile='NewUIClass.py',
                defaultextension='.py',
                filetypes=[('Python File', '*.py')]
            )
            if file:
                generator = UIClassGenerator(self.current_ui_tree)
                head, tail = os.path.split(file.name)
                class_name = os.path.splitext(tail)[0]
                generator.set_class_name(class_name)
                ret = generator.write_to_file(file)
                if ret:
                    self.console.write_info('Class generated as ' + file.name + '.')
                else:
                    raise ValueError('Failed to generate code')
                file.close()
        except Exception as e:
            mb.showerror('Error', f'Failed to generate code: {str(e)}')
            self.console.write_error(f'Failed to generate code: {str(e)}')

    def on_undo(self, event):
        """Handle undo action"""
        if self.current_ui_tree.undo():
            self.ui_updated()
            self.console.write_info('Undo successful')
        else:
            self.console.write_info('Nothing to undo')

    def on_redo(self, event):
        """Handle redo action"""
        if self.current_ui_tree.redo():
            self.ui_updated()
            self.console.write_info('Redo successful')
        else:
            self.console.write_info('Nothing to redo')

import tkinter as tk
import copy

class AttributeEditor(tk.LabelFrame):

    main_canvas = None
    scrollbar = None
    selected_object_uid = None
    selected_object_attributes = None
    working_object_attributes = None
    drawn_objects = []
    save_button = None
    delete_button = None

    def __init__(self, master=None, app=None):
        super().__init__(master, text='Attributes')
        self.app = app
        self.init_ui()

    def init_ui(self):
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        
        self.main_canvas = tk.Canvas(self)
        self.main_canvas.grid(row=0, column=0, sticky='news')
        
        self.scrollbar = tk.Scrollbar(self)
        self.scrollbar.grid(row=0, column=1, sticky='news')
        
        self.main_canvas.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.main_canvas.yview)
        
        self.draw_editor()
        
    def clear_selected_object(self):
        self.selected_object_uid = None
        self.selected_object_attributes = None
        del self.working_object_attributes
        self.draw_editor()

    def on_object_selected(self, object_uid):
        self.selected_object_uid = object_uid
        self.get_selected_object_attributes()
        self.draw_editor()
        
    def clean_canvas(self):
        for item in self.main_canvas.winfo_children():
            item.destroy()

    def draw_editor(self):
        self.clean_canvas()
        
        if self.selected_object_uid is None:
            empty_label = tk.Label(self.main_canvas, text='NO OBJECT SELECTED', fg='red')
            empty_label.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
            return
            
        for attribute_class_index in range(len(self.working_object_attributes)):
            attribute_labelframe = tk.LabelFrame(self.main_canvas, text=self.working_object_attributes[attribute_class_index]['attribute_class_name'])
            attribute_labelframe.pack(side= tk.TOP, fill=tk.BOTH)

            attributes = self.working_object_attributes[attribute_class_index]['parameters']
            for current_attribute in attributes:
                attribute_frame = tk.Frame(attribute_labelframe)
                attribute_frame.rowconfigure(0, weight=1)
                attribute_frame.columnconfigure(0, weight=2, uniform="x")
                attribute_frame.columnconfigure(1, weight=3, uniform="x")
                attribute_frame.pack(side=tk.TOP, fill=tk.X)

                attribute_name_label = tk.Label(attribute_frame, text=(current_attribute + ':'))
                attribute_name_label.grid(row=0, column=0, sticky='news')

                attribute_value_obj, attribute_value_var = self.draw_attribute_widgets(attribute_frame, self.working_object_attributes[attribute_class_index]['parameters'][current_attribute])
                attribute_value_obj.grid(row=0, column=1, sticky='news')

                self.working_object_attributes[attribute_class_index]['parameters'][current_attribute]['selector_obj'] = attribute_value_obj
                self.working_object_attributes[attribute_class_index]['parameters'][current_attribute]['selector_var'] = attribute_value_var

        # add save and delete buttons to the bottom
        self.save_button = tk.Button(self.main_canvas, text='SAVE', command=self.on_click_save)
        self.save_button.pack(side=tk.TOP, fill=tk.BOTH)
        
        self.delete_button = tk.Button(self.main_canvas, text='DELETE', command=self.on_click_delete)
        self.delete_button.pack(side=tk.TOP, fill=tk.BOTH)
    
    def draw_attribute_widgets(self, frame, attribute_data):
        attribute_type = attribute_data['type']
        
        new_obj = None
        var = None
        
        if attribute_type == 'constant':
            var = tk.StringVar(frame, value=str(attribute_data['value']))
            new_obj = tk.Label(frame, text=str(attribute_data['value']))
        if attribute_type == 'integer':
            var = tk.IntVar(frame, value=int(attribute_data['value']))
            new_obj = tk.Entry(frame, textvariable=var)
        if attribute_type == 'string':
            var = tk.StringVar(frame, value=attribute_data['value'])
            new_obj = tk.Entry(frame, textvariable=var)
        if attribute_type == 'boolean':
            var = tk.IntVar(frame, value=int(attribute_data['value']))
            new_obj = tk.Checkbutton(frame, variable=var)
        if attribute_type == 'select':
            var = tk.StringVar(frame, value=attribute_data['value'])
            new_obj = tk.OptionMenu(frame, var, *attribute_data['options'])
        return new_obj, var

    def get_selected_object_attributes(self):
        self.selected_object_attributes = self.app.get_object_attributes(self.selected_object_uid)
        self.working_object_attributes = copy.deepcopy(self.selected_object_attributes)

    def set_current_object_attributes(self):
        self.app.set_object_attributes(self.selected_object_uid, self.selected_object_attributes)

    def on_click_save(self):
        for attribute_class_index in range(len(self.working_object_attributes)):
            attributes = self.working_object_attributes[attribute_class_index]['parameters']
            for current_attribute in attributes:

                value = str(self.working_object_attributes[attribute_class_index]['parameters'][current_attribute]['selector_var'].get())
                self.working_object_attributes[attribute_class_index]['parameters'][current_attribute]['value'] = value
                del self.working_object_attributes[attribute_class_index]['parameters'][current_attribute]['selector_obj']
                del self.working_object_attributes[attribute_class_index]['parameters'][current_attribute]['selector_var']
                    
        self.app.set_object_attributes(self.selected_object_uid, self.working_object_attributes)
        uid = self.selected_object_uid
        self.clear_selected_object()
        self.on_object_selected(uid)
                
    def on_click_delete(self):
        self.app.on_delete_object_click(self.selected_object_uid)

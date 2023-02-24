import tkinter as tk

class PlaceObjectSelector(tk.LabelFrame):
    
    main_canvas = None
    scrollbar = None
    listed_object_buttons = {}
    selected_object = None
    
    def __init__(self, master=None, app=None):
        super().__init__(master, text='Place')
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
        
        self.create_widgets(self.main_canvas)

    def create_widgets(self, main_canvas):
        types = []
        objects_data = self.app.get_objects_data()
        
        for obj in objects_data:
            if objects_data[obj]['type'] not in types:
                types.append(objects_data[obj]['type'])
        
        for t in types:
            type_label = tk.Label(main_canvas, text=t.upper(), fg='red')
            type_label.pack(fill=tk.BOTH)
            
            buttons = []
            for obj in objects_data:
                if objects_data[obj]['type'] == t:
                    buttons.append(tk.Button(main_canvas, text=obj, command=lambda name=obj: self.on_button_press(name)))
                    buttons[-1].pack(fill=tk.BOTH)

            self.listed_object_buttons[t] = buttons

    def clear_selected_object(self):
        self.selected_object = None
        
        for t in self.listed_object_buttons:
            for button in self.listed_object_buttons[t]:
                button.config(relief=tk.RAISED)        

    def on_button_press(self, obj):
        if self.selected_object == obj:
            self.clear_selected_object()
        else:
            self.selected_object = obj
            for t in self.listed_object_buttons:
                for button in self.listed_object_buttons[t]:
                    if button['text'] != obj:
                        button.config(relief=tk.RAISED)
                    else:
                        button.config(relief=tk.SUNKEN)

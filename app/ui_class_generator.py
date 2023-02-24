from .ui_tree import UITree
from .ui_node import UINode
from .code_generator import CodeGenerator

class UIClassGenerator:

    callback_attributes = ['command']

    def __init__(self, ui_tree = None, class_name="GeneratedClass"):
        self.current_ui_tree = ui_tree
        self.class_name = class_name
        self.codegen = CodeGenerator()

    def set_class_name(self, name):
        self.class_name = name
        
    def generate_class_code(self):
        self.generate_file_header()
        
        nodes = self.current_ui_tree.get_all_nodes()
        
        # generate widgets
        for uid, node in nodes.items():
            if uid == '0':
                continue
            self.generate_widget_code(uid, node)
        
        self.codegen.dedent()

        # generate callback methods
        for uid, node in nodes.items():
            self.generate_callback_methods(uid, node)
        

    def generate_file_header(self):
        # import and class definition
        self.codegen.line('import tkinter as tk')
        self.codegen.line('import tkinter.ttk as ttk')
        self.codegen.line('')
        self.codegen.line('class {classname}(tk.{container_type}):'.format(classname=self.class_name, container_type=self.current_ui_tree.get_node('0').get_node_type()))
        self.codegen.line('')
        self.codegen.indent()
        
        # constructor
        self.codegen.line('def __init__(self, master=None):')
        self.codegen.indent()
        self.codegen.line('super().__init__(master)')
        self.codegen.line('self.init_ui()')
        self.codegen.dedent()
        self.codegen.line('')
        
        # init_ui
        self.codegen.line('def init_ui(self):')
        self.codegen.indent()

    def generate_widget_code(self, uid, node):
        parent_node = self.current_ui_tree.get_parent_node(uid)
        parent_name = parent_node.get_node_name() if (node.get_parent() != '0') else ('self')
        widget_attributes_list = node.get_attributes_list()

        # create widget
        create_string = ''
        parent_string = 'self' if (node.get_parent() == '0') else 'self.{parent_name}'.format(parent_name=parent_name)
        create_string += 'self.{object_name} = {lib_type}.{widget_type}({parent_name}'.format(lib_type=node.get_node_lib_type(), object_name=node.get_node_name(), widget_type=node.get_node_type(), parent_name=parent_string)

        for key_name, key_value in widget_attributes_list[3]['parameters'].items():
            if key_name in self.callback_attributes and key_value['value'] != "":
                create_string += ', {callback_name}=self.{callback_value}'.format(callback_name=key_name, callback_value=key_value['value'])

        create_string += ')'
        self.codegen.line(create_string)

        # configure paremeters
        for key_name, key_value in widget_attributes_list[3]['parameters'].items():
            if key_name not in self.callback_attributes:
                self.codegen.line('self.{object_name}.configure({key_name}="{key_value}")'.format(object_name=node.get_node_name(), key_name=key_name, key_value=key_value['value']))
        
        # set layout
        layout_string = ''
        if 'grid' == parent_node.get_attributes_list()[4]['parameters']['type']['value']:
            pass
        else:
            layout_string += 'self.{object_name}.pack('.format(object_name=node.get_node_name())
            pack_string = ''
            for key_name, key_value in widget_attributes_list[2]['parameters'].items():
                if pack_string != '':
                    pack_string += ', '
                pack_string += '{key_name}="{key_value}"'.format(key_name=key_name, key_value=key_value['value'])
            layout_string += pack_string

        layout_string += ')'
        self.codegen.line(layout_string)

        self.codegen.line('')

        

    def generate_callback_methods(self, uid, node):
        widget_attributes_list = node.get_attributes_list()
        for key_name, key_value in widget_attributes_list[3]['parameters'].items():
            if key_name in self.callback_attributes and key_value['value'] != "":
                self.codegen.line('def {callback_fname}(self):'.format(callback_fname=key_value['value']))
                self.codegen.indent()
                self.codegen.line('pass')
                self.codegen.dedent()
                self.codegen.line('')
        

    def write_to_file(self, file):
        if file is not None:
            self.generate_class_code()
            file.write(self.codegen.get_code())
            print(self.codegen.get_code())

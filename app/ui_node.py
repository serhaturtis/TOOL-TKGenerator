import copy

from app.objects_data import *

class UINode:
    
    def __init__(self, node_type, uid, parent_uid=None, children_list=[], attributes_list=None, app=None):
        self.app = app
        self.node_type = node_type
        self.uid = uid
        self.parent_uid = parent_uid
        self.children_list = children_list
        self.attributes_list = copy.deepcopy(attributes_list)

    def is_container(self):
        return ('container' == self.app.get_objects_data()[self.node_type]['type'])

    def add_child(self, uid):
        if self.children_list is None:
            self.children_list = []
        self.children_list.append(uid)

    def remove_child(self, uid):
        self.children_list.remove(uid)

    def get_children(self):
        return self.children_list

    def set_children(self, children_list):
        self.children_list = children_list

    def get_parent(self):
        return self.parent_uid

    def get_node_type(self):
        return self.node_type
        
    def get_attributes_list(self):
        return self.attributes_list
        
    def set_attributes_list(self, attributes_list):
        self.attributes_list = copy.deepcopy(attributes_list)
        
    def get_node_name(self):
        return self.attributes_list[ATTR_INDEX_OBJECT]['parameters']['name']['value']

    def get_node_lib_type(self):
        return self.app.get_objects_data()[self.node_type]['lib']

    def serialize(self):
        data = {}
        data['node_type'] = self.node_type
        data['parent_uid'] = self.parent_uid
        data['children_list'] = self.children_list
        data['attributes_list'] = copy.deepcopy(self.attributes_list)
        return data

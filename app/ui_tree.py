import random
import json
import copy

from app.ui_node import UINode

class UITree:
    
    app = None
    master_container = None
    
    def __init__(self, app=None):
        self.app = app
        self.nodes = {}
        self.node_count = 0
        self.add_master_frame()
        
    def add_master_frame(self):
        attributes_list = copy.deepcopy(self.app.get_object_attributes_list('Frame'))
        attributes_list[0]['parameters']['uid']['value'] = '0'
        attributes_list[0]['parameters']['name']['value'] = 'object_' + '0'
        children_list = []
        self.master_container = UINode('Frame', '0', None, children_list, attributes_list, self.app)
        self.nodes['0'] = self.master_container

    def add_node(self, node_type, parent_uid):
        parent_node = self.nodes[parent_uid]
        
        if parent_node.is_container():
            uid = self.generate_uid()

            attributes_list = copy.deepcopy(self.app.get_object_attributes_list(node_type))
            attributes_list[0]['parameters']['uid']['value'] = uid
            attributes_list[0]['parameters']['name']['value'] = 'object_' + uid

            # check layout parameters
            if 'grid' == parent_node.get_attributes_list()[4]['parameters']['type']['value']:
                print('Parent is grid.')
            else:
                print('Parent is pack.')


            object_node = UINode(node_type, uid, parent_uid, [], attributes_list, self.app)
            parent_node.add_child(uid)
            self.nodes[uid] = object_node
            return uid
        else:
            return None

    def remove_node(self, uid):
        object_node = self.nodes[uid]
        if object_node.is_container():
            children_list = object_node.get_children().copy()
            if children_list is not None:
                for child in children_list:
                    self.remove_node(child)
        
        parent_uid = object_node.get_parent()
        self.nodes[parent_uid].remove_child(uid)
        del self.nodes[uid]

    def get_node(self, uid):
        return self.nodes[uid]
        
    def get_parent_node(self, uid):
        return self.nodes[self.nodes[uid].get_parent()]

    def get_all_nodes(self):
        return self.nodes
        
    def get_node_attributes(self, uid):
        return self.nodes[uid].get_attributes_list()
        
    def set_node_attributes(self, uid, attributes_list):
        self.nodes[uid].set_attributes_list(attributes_list)

    def get_node_type(self, uid):
        return self.nodes[uid].get_node_type()

    def generate_uid(self):
        while True:
            self.node_count += 1
            uid = str(self.node_count)
            if uid not in self.nodes:
                return uid

    def serialize(self):
        data = {}
        for uid, obj in self.nodes.items():
            data[uid] = obj.serialize()
        return json.dumps(data, sort_keys=False, indent=4)

    def deserialize(self, data):
        try:
            data = json.loads(data)
            new_objects_list = {}
            for uid, obj in data.items():
                object_node = None
                node_type = obj['node_type']
                parent_uid = obj['parent_uid']
                children_list = obj['children_list']
                attributes_list = copy.deepcopy(obj['attributes_list'])

                object_node = UINode(node_type, uid, parent_uid, children_list, attributes_list, self.app)
                if uid == '0':
                    self.master_container = object_node
                
                new_objects_list[uid] = object_node
                self.node_count += 1

            self.nodes = new_objects_list
            return 1
        except:
            return 0

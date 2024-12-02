import copy
from typing import Dict, Any, Optional, List

from app.objects_data import *

class UINode:
    
    def __init__(self, node_type: str, uid: str, parent_uid: Optional[str] = None, children_list: List[str] = [], attributes_list: Dict[str, Any] = None, app: Any = None) -> None:
        self.app = app
        self.node_type = node_type
        self.uid = uid
        self.parent_uid = parent_uid
        self.children_list: List[str] = children_list
        self.attributes_list: Dict[str, Any] = copy.deepcopy(attributes_list)

    def is_container(self) -> bool:
        return ('container' == self.app.get_objects_data()[self.node_type]['type'])

    def add_child(self, uid: str) -> None:
        if self.children_list is None:
            self.children_list = []
        self.children_list.append(uid)

    def remove_child(self, uid: str) -> None:
        self.children_list.remove(uid)

    def get_children(self) -> List[str]:
        return self.children_list

    def set_children(self, children_list: List[str]) -> None:
        self.children_list = children_list

    def get_parent(self) -> Optional[str]:
        return self.parent_uid

    def get_node_type(self) -> str:
        return self.node_type
        
    def get_attributes_list(self) -> Dict[str, Any]:
        return self.attributes_list
        
    def set_attributes_list(self, attributes_list: Dict[str, Any]) -> None:
        self.attributes_list = copy.deepcopy(attributes_list)
        
    def get_node_name(self) -> str:
        return self.attributes_list[ATTR_INDEX_OBJECT]['parameters']['name']['value']

    def get_node_lib_type(self) -> str:
        return self.app.get_objects_data()[self.node_type]['lib']

    def get_uid(self) -> str:
        """Get the unique identifier of this node"""
        return self.uid

    def serialize(self) -> Dict[str, Any]:
        data = {}
        data['node_type'] = self.node_type
        data['parent_uid'] = self.parent_uid
        data['children_list'] = self.children_list
        data['attributes_list'] = copy.deepcopy(self.attributes_list)
        return data

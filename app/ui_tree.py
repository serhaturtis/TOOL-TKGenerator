import random
import json
import copy
from typing import Dict, Any, Optional, List

from app.objects_data import *
from .ui_node import UINode
from .undo_manager import UndoManager, UndoAction

class UITree:
    
    app: Any = None
    master_container: UINode = None
    
    def __init__(self, app: Any = None) -> None:
        self.app = app
        self.nodes: Dict[str, UINode] = {}
        self.node_count: int = 0
        self.undo_manager = UndoManager()
        self.add_master_frame()
        
    def add_master_frame(self) -> None:
        attributes_list = copy.deepcopy(self.app.get_object_attributes_list('Frame'))
        attributes_list[ATTR_INDEX_OBJECT]['parameters']['uid']['value'] = '0'
        attributes_list[ATTR_INDEX_OBJECT]['parameters']['name']['value'] = 'object_' + '0'
        children_list: List[str] = []
        self.master_container = UINode('Frame', '0', None, children_list, attributes_list, self.app)
        self.nodes['0'] = self.master_container

    def _create_node_state(self, node: UINode) -> Dict[str, Any]:
        """Create a serializable state of a node and its children"""
        state = {
            'node_type': node.get_node_type(),
            'attributes': copy.deepcopy(node.get_attributes_list()),
            'children': []
        }
        
        # If this is a container, store the complete state of all children
        if node.is_container():
            for child_uid in node.get_children():
                if child_uid in self.nodes:
                    child_node = self.nodes[child_uid]
                    child_state = {
                        'uid': child_uid,
                        'state': self._create_node_state(child_node)
                    }
                    state['children'].append(child_state)
        
        return state

    def _restore_node_state(self, uid: str, state: Dict[str, Any], parent_uid: str) -> None:
        """Restore a node and its children from a saved state"""
        node_type = state['node_type']
        attributes = copy.deepcopy(state['attributes'])
        
        # Create the node first
        node = UINode(node_type, uid, parent_uid, [], attributes, self.app)
        self.nodes[uid] = node
        
        # Add it to its parent
        if parent_uid is not None and parent_uid in self.nodes:
            self.nodes[parent_uid].add_child(uid)
        
        # Then restore all its children if it's a container
        if node.is_container() and 'children' in state and state['children']:
            for child in state['children']:
                child_uid = child['uid']
                self._restore_node_state(child_uid, child['state'], uid)

    def add_node(self, node_type: str, parent_uid: str) -> Optional[str]:
        parent_node = self.nodes[parent_uid]
        
        if parent_node.is_container():
            uid = self.generate_uid()

            attributes_list = copy.deepcopy(self.app.get_object_attributes_list(node_type))
            attributes_list[ATTR_INDEX_OBJECT]['parameters']['uid']['value'] = uid
            attributes_list[ATTR_INDEX_OBJECT]['parameters']['name']['value'] = 'object_' + uid
            children_list = []
            
            new_node = UINode(node_type, uid, parent_uid, children_list, attributes_list, self.app)
            self.nodes[uid] = new_node
            parent_node.add_child(uid)

            # Record action with empty old state
            self._record_action(
                action_type='add',
                node_uid=uid,
                old_state={},
                new_state=self._create_node_state(new_node),
                parent_uid=parent_uid
            )
            
            return uid
        return None

    def remove_node(self, uid: str) -> None:
        """Remove a node from the tree"""
        if uid not in self.nodes or uid == '0':  # Can't remove root
            return
            
        node = self.nodes[uid]
        if not node or not node.get_parent():
            return
            
        parent_uid = node.get_parent()
        if parent_uid not in self.nodes:
            return
            
        # Create state snapshots before removal
        old_state = self._create_node_state(node)
        
        # Remove the node and its children
        self._remove_container_node(node)
        
        # Record the action for undo/redo
        self._record_action('remove', uid, old_state, {}, parent_uid)
        
        # Update UI
        if self.app:
            self.app.ui_updated()

    def set_node_attributes(self, uid: str, attributes_list: Dict[str, Any]) -> None:
        node = self.nodes[uid]
        old_attributes = copy.deepcopy(node.get_attributes_list())
        
        # Record action before modifying
        self._record_action(
            action_type='modify',
            node_uid=uid,
            old_state={'attributes': old_attributes},
            new_state={'attributes': copy.deepcopy(attributes_list)}
        )
        
        node.set_attributes_list(attributes_list)

    def apply_undo_action(self, action: UndoAction, is_undo: bool) -> None:
        """Apply an undo/redo action"""
        if not action:
            return
            
        # For undo, we want to go from current (new) state to old state
        # For redo, we want to go from current (old) state to new state
        target_state = action.old_state if is_undo else action.new_state
        
        if not action.node_uid or not action.parent_uid:
            return
            
        if action.action_type == 'add':
            if is_undo:  # Undo add = remove
                if action.node_uid in self.nodes:
                    node = self.nodes[action.node_uid]
                    self._remove_container_node(node)
            else:  # Redo add = create
                if action.node_uid not in self.nodes:
                    self._restore_node_state(action.node_uid, target_state, action.parent_uid)

        elif action.action_type == 'remove':
            if is_undo:  # Undo remove = create
                if action.node_uid not in self.nodes:
                    self._restore_node_state(action.node_uid, target_state, action.parent_uid)
            else:  # Redo remove = remove
                if action.node_uid in self.nodes:
                    node = self.nodes[action.node_uid]
                    self._remove_container_node(node)

        elif action.action_type == 'modify':
            if action.node_uid in self.nodes:
                attributes = copy.deepcopy(target_state['attributes'])
                self.nodes[action.node_uid].set_attributes_list(attributes)
                
        # Ensure UI is updated after any undo/redo action
        if self.app:
            self.app.ui_updated()

    def _remove_container_node(self, node: UINode) -> None:
        """Safely remove a container node and all its children"""
        if not node:
            return
            
        parent_uid = node.get_parent()
        if not parent_uid or parent_uid not in self.nodes:
            return
            
        node_uid = node.get_uid()
            
        # First remove all children recursively
        if node.is_container():
            children = node.get_children().copy()  # Make a copy as we'll modify the list
            for child_uid in children:
                if child_uid in self.nodes:
                    child_node = self.nodes[child_uid]
                    self._remove_container_node(child_node)
        
        # Then remove the node itself from its parent
        self.nodes[parent_uid].remove_child(node_uid)
        # And delete it from nodes dictionary
        del self.nodes[node_uid]

    def undo(self) -> bool:
        """Undo the last action"""
        return self.undo_manager.undo(self.apply_undo_action) is not None

    def redo(self) -> bool:
        """Redo the last undone action"""
        return self.undo_manager.redo(self.apply_undo_action) is not None

    def can_undo(self) -> bool:
        """Check if undo is available"""
        return self.undo_manager.can_undo()

    def can_redo(self) -> bool:
        """Check if redo is available"""
        return self.undo_manager.can_redo()

    def get_node(self, uid: str) -> UINode:
        return self.nodes[uid]
        
    def get_parent_node(self, uid: str) -> UINode:
        return self.nodes[self.nodes[uid].get_parent()]

    def get_all_nodes(self) -> Dict[str, UINode]:
        return self.nodes
        
    def get_node_attributes(self, uid: str) -> Dict[str, Any]:
        return self.nodes[uid].get_attributes_list()
        
    def get_node_type(self, uid: str) -> str:
        return self.nodes[uid].get_node_type()

    def generate_uid(self) -> str:
        while True:
            self.node_count += 1
            uid = str(self.node_count)
            if uid not in self.nodes:
                return uid

    def deserialize(self, data: str) -> bool:
        try:
            data = json.loads(data)
            new_objects_list = {}
            
            # Clear undo/redo stacks when loading new UI
            self.undo_manager.clear()
            
            # First pass: create all nodes
            for uid, obj in data.items():
                node_type = obj['node_type']
                parent_uid = obj['parent_uid']
                children_list = obj.get('children_list', [])
                attributes_list = obj.get('attributes_list', None)
                
                node = UINode(node_type, uid, parent_uid, children_list, attributes_list, self.app)
                new_objects_list[uid] = node
                self.node_count = max(self.node_count, int(uid))
                
            # Clear existing nodes and replace with new ones
            self.nodes.clear()
            self.nodes.update(new_objects_list)
            return True
            
        except Exception as e:
            print(f"Error deserializing UI tree: {str(e)}")
            return False

    def _record_action(self, action_type: str, node_uid: str, old_state: Dict[str, Any], new_state: Dict[str, Any], parent_uid: Optional[str] = None) -> None:
        """Record an action for undo/redo"""
        action = UndoAction(
            action_type=action_type,
            node_uid=node_uid,
            old_state=old_state,
            new_state=new_state,
            parent_uid=parent_uid
        )
        self.undo_manager.push_action(action)

    def serialize(self) -> str:
        data = {}
        for uid, obj in self.nodes.items():
            data[uid] = obj.serialize()
        return json.dumps(data, sort_keys=False, indent=4)

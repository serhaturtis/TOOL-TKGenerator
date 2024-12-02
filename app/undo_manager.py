from typing import List, Dict, Any, Optional, Callable
from dataclasses import dataclass
import json

@dataclass
class UndoAction:
    """Represents a single undoable action"""
    action_type: str  # 'add', 'remove', 'modify'
    node_uid: str
    old_state: Dict[str, Any]
    new_state: Dict[str, Any]
    parent_uid: Optional[str] = None

class UndoManager:
    def __init__(self, max_history: int = 50):
        self.undo_stack: List[UndoAction] = []
        self.redo_stack: List[UndoAction] = []
        self.max_history = max_history
        self._in_progress = False
        
    def clear(self) -> None:
        """Clear all undo/redo history"""
        self.undo_stack.clear()
        self.redo_stack.clear()
        
    def push_action(self, action: UndoAction) -> None:
        """Add a new action to the undo stack"""
        if self._in_progress:
            return
            
        self.redo_stack.clear()  # Clear redo stack when new action is added
        self.undo_stack.append(action)
        
        # Keep stack within size limit
        while len(self.undo_stack) > self.max_history:
            self.undo_stack.pop(0)
            
    def can_undo(self) -> bool:
        """Check if undo is available"""
        return len(self.undo_stack) > 0
        
    def can_redo(self) -> bool:
        """Check if redo is available"""
        return len(self.redo_stack) > 0
        
    def undo(self, apply_func: Callable[[UndoAction, bool], None]) -> Optional[UndoAction]:
        """Undo the last action"""
        if not self.can_undo():
            return None
            
        self._in_progress = True
        try:
            action = self.undo_stack.pop()
            apply_func(action, True)  # True for undo
            self.redo_stack.append(action)
            return action
        finally:
            self._in_progress = False
            
    def redo(self, apply_func: Callable[[UndoAction, bool], None]) -> Optional[UndoAction]:
        """Redo the last undone action"""
        if not self.can_redo():
            return None
            
        self._in_progress = True
        try:
            action = self.redo_stack.pop()
            apply_func(action, False)  # False for redo
            self.undo_stack.append(action)
            return action
        finally:
            self._in_progress = False

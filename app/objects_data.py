LAYOUT_MANAGER_ATTRIBUTES = {
	"attribute_class_name": "Layout Manager",
	"parameters": {
		"type": {
			"type": "select",
			"options": ["pack", "grid"],
			"value": "pack"
		},
        "rweights": {
			"type": "int_array",
            "value": "0,0"
		},
        "cweights": {
			"type": "int_array",
            "value": "0,0"
		}
	}
}

WIDGET_GRID_LAYOUT_ATTRIBUTES = {
	"attribute_class_name": "Grid",
	"parameters": {
		"row": {
			"type": "integer",
			"value": "0"
		},
		"column": {
			"type": "integer",
			"value": "0"
		},
		"sticky": {
			"type": "string",
			"value": "nsew"
		}
	}
}

WIDGET_PACK_LAYOUT_ATTRIBUTES = {
	"attribute_class_name": "Pack",
	"parameters": {
		"side": {
			"type": "select",
			"options": ["left", "right", "top", "bottom"],
			"value": "left"
		},
		"fill": {
			"type": "select",
			"options": ["none", "x", "y", "both"],
			"value": "both"
		},
		"expand": {
			"type": "boolean",
			"value": "0"
		}
	}
}

OBJECT_ATTRIBUTES = {
	"attribute_class_name": "Object",
	"parameters": {
		"name": {
			"type": "string",
			"value": "object"
		},
		"uid":{
			"type": "constant",
			"value": ""
		}
	}
}

PLACEMENT_ATTRIBUTES = {
    "attribute_class_name": "Placement",
    "parameters": {
		"padx": {
			"type": "integer",
			"value": "5"
		},
		"pady": {
			"type": "integer",
			"value": "5"
		},
		"ipadx": {
			"type": "integer",
			"value": "5"
		},
		"ipady": {
			"type": "integer",
			"value": "5"
		}
	}
}

FRAME_ATTRIBUTES = {
	"attribute_class_name": "Frame",
	"parameters": {

	}
}

CANVAS_ATTRIBUTES = {
	"attribute_class_name": "Canvas",
	"parameters": {

	}
}

LABELFRAME_ATTRIBUTES = {
	"attribute_class_name": "LabelFrame",
	"parameters": {
		"text": {
			"type": "string",
			"value": "LabelFrame"
		}
	}
}

BUTTON_ATTRIBUTES = {
	"attribute_class_name": "Button",
	"parameters": {
		"text": {
			"type": "string",
			"value": "Button"
		},
		"command": {
			"type": "string",
			"value": ""
		}
	}
}

CHECKBUTTON_ATTRIBUTES = {
	"attribute_class_name": "Checkbutton",
	"parameters": {
		"text": {
			"type": "string",
			"value": "Checkbutton"
		},
		"command": {
			"type": "string",
			"value": ""
		}
	}
}

ENTRY_ATTRIBUTES = {
	"attribute_class_name": "Entry",
	"parameters": {
		"show": {
			"type": "string",
			"value": ""
		},
		"command": {
			"type": "string",
			"value": ""
		}
	}
}

LABEL_ATTRIBUTES = {
	"attribute_class_name": "Label",
	"parameters": {
		"text": {
			"type": "string",
			"value": "Label"
		}
	}
}

LISTBOX_ATTRIBUTES = {
	"attribute_class_name": "Listbox",
	"parameters": {

	}
}

RADIOBUTTON_ATTRIBUTES = {
	"attribute_class_name": "Radiobutton",
	"parameters": {
		"text": {
			"type": "string",
			"value": "Radiobutton"
		},
		"command": {
			"type": "string",
			"value": ""
		}
	}
}

SCROLLBAR_ATTRIBUTES = {
	"attribute_class_name": "Scrollbar",
	"parameters": {
		"orient": {
			"type": "select",
			"options": ["vertical", "horizontal"],
			"value": "vertical"
		}
	}
}

SPINBOX_ATTRIBUTES = {
	"attribute_class_name": "Spinbox",
	"parameters": {

	}
}

TEXT_ATTRIBUTES = {
	"attribute_class_name": "Text",
	"parameters": {

	}
}

COMBOBOX_ATTRIBUTES = {
    "attribute_class_name": "Combobox",
    "parameters": {
		
	}
}

NOTEBOOK_ATTRIBUTES = {
    "attribute_class_name": "Notebook",
    "parameters": {
		
	}
}

PROGRESSBAR_ATTRIBUTES = {
    "attribute_class_name": "Progressbar",
    "parameters": {
		
	}
}

SEPARATOR_ATTRIBUTES = {
    "attribute_class_name": "Separator",
    "parameters": {
		
	}
}

SIZEGRIP_ATTRIBUTES = {
    "attribute_class_name": "Sizegrip",
    "parameters": {
		
	}
}

TREEVIEW_ATTRIBUTES = {
    "attribute_class_name": "Treeview",
    "parameters": {
		
	}
}

OBJECTS_DATA = {
	"Frame": {
		"type": "container",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, FRAME_ATTRIBUTES, LAYOUT_MANAGER_ATTRIBUTES]
	},
	"Canvas": {
		"type": "container",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, CANVAS_ATTRIBUTES, LAYOUT_MANAGER_ATTRIBUTES]
	},
	"LabelFrame": {
		"type": "container",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, LABELFRAME_ATTRIBUTES, LAYOUT_MANAGER_ATTRIBUTES]
	},
	"Button": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, BUTTON_ATTRIBUTES]
	},
	"Checkbutton": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, CHECKBUTTON_ATTRIBUTES]
	},
	"Entry": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, ENTRY_ATTRIBUTES]
	},
	"Label": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, LABEL_ATTRIBUTES]
	},
	"Listbox": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, LISTBOX_ATTRIBUTES]
	},
	"Radiobutton": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, RADIOBUTTON_ATTRIBUTES]
	},
	"Scrollbar": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, SCROLLBAR_ATTRIBUTES]
	},
	"Text": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, TEXT_ATTRIBUTES]
	},
    "Combobox": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, COMBOBOX_ATTRIBUTES]
	},
    "Spinbox": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, SPINBOX_ATTRIBUTES]
	},
    "Notebook": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, NOTEBOOK_ATTRIBUTES]
	},
    "Progressbar": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, PROGRESSBAR_ATTRIBUTES]
	},
    "Separator": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, SEPARATOR_ATTRIBUTES]
	},
    "Sizegrip": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, SIZEGRIP_ATTRIBUTES]
	},
    "Treeview": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [OBJECT_ATTRIBUTES, PLACEMENT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, TREEVIEW_ATTRIBUTES]
	}
}

ATTR_INDEX_OBJECT = 0
ATTR_INDEX_PLACE = 1
ATTR_INDEX_GRID = 2
ATTR_INDEX_PACK = 3
ATTR_INDEX_SPEC = 4
ATTR_INDEX_LAYOUT = 5
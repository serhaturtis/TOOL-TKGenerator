LAYOUT_MANAGER_ATTRIBUTES = {
	"attribute_class_name": "Layout Manager Attributes",
	"parameters": {
		"type": {
			"type": "select",
			"options": ["pack", "grid"],
			"value": "pack"
		}
	}
}

WIDGET_GRID_LAYOUT_ATTRIBUTES = {
	"attribute_class_name": "Widget Grid Layout Attributes",
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
		},
		"padx": {
			"type": "integer",
			"value": "10"
		},
		"pady": {
			"type": "integer",
			"value": "10"
		},
		"ipadx": {
			"type": "integer",
			"value": "10"
		},
		"ipady": {
			"type": "integer",
			"value": "10"
		}
	}
}

WIDGET_PACK_LAYOUT_ATTRIBUTES = {
	"attribute_class_name": "Widget Pack Layout Attributes",
	"parameters": {
		"side": {
			"type": "select",
			"options": ["left", "right", "top", "bottom"],
			"value": "left"
		},
		"fill": {
			"type": "select",
			"options": ["none", "x", "y", "both"],
			"value": "none"
		},
		"expand": {
			"type": "boolean",
			"value": "1"
		},
		"padx": {
			"type": "integer",
			"value": "10"
		},
		"pady": {
			"type": "integer",
			"value": "10"
		},
		"ipadx": {
			"type": "integer",
			"value": "10"
		},
		"ipady": {
			"type": "integer",
			"value": "10"
		}
	}
}

GENERIC_OBJECT_ATTRIBUTES = {
	"attribute_class_name": "Generic Object Attributes",
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

FRAME_ATTRIBUTES = {
	"attribute_class_name": "Frame Attributes",
	"parameters": {

	}
}

CANVAS_ATTRIBUTES = {
	"attribute_class_name": "Canvas Attributes",
	"parameters": {

	}
}

LABELFRAME_ATTRIBUTES = {
	"attribute_class_name": "LabelFrame Attributes",
	"parameters": {
		"text": {
			"type": "string",
			"value": "LabelFrame"
		}
	}
}

BUTTON_ATTRIBUTES = {
	"attribute_class_name": "Button Attributes",
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
	"attribute_class_name": "Checkbutton Attributes",
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
	"attribute_class_name": "Entry Attributes",
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
	"attribute_class_name": "Label Attributes",
	"parameters": {
		"text": {
			"type": "string",
			"value": "Label"
		}
	}
}

LISTBOX_ATTRIBUTES = {
	"attribute_class_name": "Listbox Attributes",
	"parameters": {

	}
}

RADIOBUTTON_ATTRIBUTES = {
	"attribute_class_name": "Radiobutton Attributes",
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
	"attribute_class_name": "Scrollbar Attributes",
	"parameters": {

	}
}

SPINBOX_ATTRIBUTES = {
	"attribute_class_name": "Spinbox Attributes",
	"parameters": {

	}
}

TEXT_ATTRIBUTES = {
	"attribute_class_name": "Text Attributes",
	"parameters": {

	}
}

COMBOBOX_ATTRIBUTES = {
    "attribute_class_name": "Combobox Attributes",
    "parameters": {
		
	}
}

NOTEBOOK_ATTRIBUTES = {
    "attribute_class_name": "Notebook Attributes",
    "parameters": {
		
	}
}

PROGRESSBAR_ATTRIBUTES = {
    "attribute_class_name": "Progressbar Attributes",
    "parameters": {
		
	}
}

SEPARATOR_ATTRIBUTES = {
    "attribute_class_name": "Separator Attributes",
    "parameters": {
		
	}
}

SIZEGRIP_ATTRIBUTES = {
    "attribute_class_name": "Sizegrip Attributes",
    "parameters": {
		
	}
}

TREEVIEW_ATTRIBUTES = {
    "attribute_class_name": "Treeview Attributes",
    "parameters": {
		
	}
}

OBJECTS_DATA = {
	"Frame": {
		"type": "container",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, FRAME_ATTRIBUTES, LAYOUT_MANAGER_ATTRIBUTES]
	},
	"Canvas": {
		"type": "container",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, CANVAS_ATTRIBUTES, LAYOUT_MANAGER_ATTRIBUTES]
	},
	"LabelFrame": {
		"type": "container",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, LABELFRAME_ATTRIBUTES, LAYOUT_MANAGER_ATTRIBUTES]
	},
	"Button": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, BUTTON_ATTRIBUTES]
	},
	"Checkbutton": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, CHECKBUTTON_ATTRIBUTES]
	},
	"Entry": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, ENTRY_ATTRIBUTES]
	},
	"Label": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, LABEL_ATTRIBUTES]
	},
	"Listbox": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, LISTBOX_ATTRIBUTES]
	},
	"Radiobutton": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, RADIOBUTTON_ATTRIBUTES]
	},
	"Scrollbar": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, SCROLLBAR_ATTRIBUTES]
	},
	"Text": {
		"type": "widget",
		"lib": "tk",
		"attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, TEXT_ATTRIBUTES]
	},
    "Combobox": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, COMBOBOX_ATTRIBUTES]
	},
    "Spinbox": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, SPINBOX_ATTRIBUTES]
	},
    "Notebook": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, NOTEBOOK_ATTRIBUTES]
	},
    "Progressbar": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, PROGRESSBAR_ATTRIBUTES]
	},
    "Separator": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, SEPARATOR_ATTRIBUTES]
	},
    "Sizegrip": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, SIZEGRIP_ATTRIBUTES]
	},
    "Treeview": {
		"type": "widget",
		"lib": "ttk",
        "attributes_list": [GENERIC_OBJECT_ATTRIBUTES, WIDGET_GRID_LAYOUT_ATTRIBUTES, WIDGET_PACK_LAYOUT_ATTRIBUTES, TREEVIEW_ATTRIBUTES]
	}
}
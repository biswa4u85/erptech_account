import frappe
from frappe import _

@frappe.whitelist()
def get_workspace_sidebar_items():
	pages = [{
        "name": "Accounting",
        "title": "Accounting",
        "for_user": "",
        "parent_page": "",
        "content": "[{\"id\":\"MmUf9abwxg\",\"type\":\"onboarding\",\"data\":{\"onboarding_name\":\"Accounts\",\"col\":12}}]",
        "public": 1,
        "module": "Accounts",
        "icon": "accounting",
        "indicator_color": "red",
        "is_hidden": 0,
        "label": "Accounting",
        "is_editable": True,
        "selected": True
    },
    ]
	return {"pages": pages, "has_access": True}
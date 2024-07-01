import frappe
from frappe.core.api.file import get_attached_images

@frappe.whitelist()
 

def handle_new_blog_post():
    def get_permission_query_conditions():
        return 'status="Active"'
pass
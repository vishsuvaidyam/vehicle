import frappe

def get_context(context):
     context.vehicle_list = frappe.get_all("vehicle",
        filters={"status":"Active"},
        fields=["make","model","year","route"],
        order_by="make")
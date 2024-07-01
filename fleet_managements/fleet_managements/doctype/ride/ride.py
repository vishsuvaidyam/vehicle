# Copyright (c) 2024, vish and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Ride(Document):
    def before_save(self):
        total = 0.0
        for a in self.cost_breakup:
            a.amount = a.distance_in_km * a.rate_per_km
            total += a.amount
        self.total_amount = total

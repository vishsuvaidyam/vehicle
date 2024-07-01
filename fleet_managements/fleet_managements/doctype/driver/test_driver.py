# Copyright (c) 2024, vish and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase

class TestDriver(FrappeTestCase):
    def test_fullname_is_set_automatically(self):
        test_driver = frappe.get_doc({
            "doctype": "Driver",
            "first_name": "Aman",
            "last_name": "Kumar",
            "dob": "2004-10-15"
        }).insert()
        self.assertEqual(test_driver.full_name, "Aman Kumar")
    
    def test_full_name_is_set_correctly_when_no_lastname(self):
        test_driver = frappe.get_doc({
            "doctype": "Driver",
            "first_name": "Aman",
            "last_name": "",
            "dob": "2004-10-15"
        }).insert()
        self.assertEqual(test_driver.full_name, "Aman")



# Assuming `full_name` is being set in the `Driver` DocType, which is typically handled in the `before_insert` or `validate` method in Frappe.

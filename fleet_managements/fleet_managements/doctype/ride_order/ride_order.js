// Copyright (c) 2024, vish and contributors
// For license information, please see license.txt

frappe.ui.form.on("Ride Order", {
	refresh(frm) {
		
		if (frm.doc.status, "New") {
			cur_frm.add_custom_button("Reject", () => {
				frm.set_value("status", "Rejected");
				frm.save();
			}, "Actions")
			cur_frm.add_custom_button("Accpted & Created Ride", () => {
				const dialog = new frappe.ui.Dialog({
					title: "Create Ride",
					fields: [
						{
							fieldtype: "Link",
							fieldname: "driver",
							label: "Select Driver",
							options: "Driver" ,// "option" corrected to "options"
							reqd:"1"
						}
					],
					primary_action_label: "Create",
					primary_action: (data) => {


						frm.set_value("status","Accepted");
						frm.save();

						const driver_name = data.driver;
						frappe.new_doc("Ride", {
							vehicle: frm.doc.vehicle,
							driver: driver_name
						});
					}
					
				});
				dialog.show();

				
			}, "Actions");
		}

	},
});

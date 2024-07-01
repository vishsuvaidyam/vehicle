// Copyright (c) 2024, vish and contributors
// For license information, please see license.txt

frappe.query_reports["Rides Revenue By Make"] = {
	"filters": [
		{
			"fieldname": "number_of_record",
			"fieldtype": "Int",
			"label": "  Number of Record",
			"default":10
		   }
	],
	onload:function(report){
		report.page.add_inner_button("My Button",() =>{
			console.log("hellow")
		})
	}
};

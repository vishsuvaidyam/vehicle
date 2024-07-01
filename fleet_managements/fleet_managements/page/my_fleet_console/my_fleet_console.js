frappe.pages['my-fleet-console'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Fleet Console',
		single_column: true
	});
}
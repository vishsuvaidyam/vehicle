import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "make",
            "label": "Make",
            "fieldtype": "Data",
            "width": 150
        },
        #  {
        #     "fieldname": "driver",
        #     "label": "Driver",
        #     "fieldtype": "data",
        #     "width": 200
        # },
        {
            "fieldname": "revenue",
            "label": "Revenue",
            "fieldtype": "Currency",
            "width": 100
        }
    ]

    rides = frappe.get_all("Ride", fields=["vehicle","total_amount" ,"vehicle.make"])

    revenue_by_make = {}
    for ride in rides:
        if ride.vehicle in revenue_by_make:
            revenue_by_make[ride.vehicle] + ride.total_amount
        else:
            revenue_by_make[ride.vehicle] = ride.total_amount
    
    # Data creation moved outside the loop
    data = [{"make": make, "revenue": revenue} for make, revenue in revenue_by_make.items()]

    # error hai puchhna hai

    num_records = filters.number_of_record or 10

    # chart pie
    chart= get_chart(data)
    return columns, data [:num_records],None, chart, None

def get_chart(data):
    return{
        "data":{
            "labels":[ d["revenue"] for d in data],
            "datasets":[{"name":"Revenue By Make","values":[d["revenue"] for d in data]}]
        },
        "type":"pie"
    }
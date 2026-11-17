{
    "name": "MRP Multi-Warehouse Landed Cost Extensions",
    "version": "17.0.1.0.0",
    "category": "Manufacturing/Inventory",
    "summary": "Automated freight landed cost splits and OWL floor barcode confirmation",
    "author": "Nathnael Tsegay Alene",
    "license": "LGPL-3",
    "depends": ["mrp", "stock_landed_costs", "stock_barcode"],
    "assets": {
        "web.assets_backend": [
            "mrp_landed_cost_ext/static/src/components/barcode_confirm.js",
        ],
    },
    "installable": True,
}

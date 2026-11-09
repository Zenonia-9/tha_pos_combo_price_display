{
    "name": "POS Combo Price Display",
    "version": "17.0.1.0.1",
    "category": "Point of Sale",
    "summary": "Show a single combo price while hiding component prices in POS and receipts",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "tha_pos_combo_price_display/static/src/js/combo_price_display.js",
            "tha_pos_combo_price_display/static/src/xml/combo_price_display.xml",
        ],
    },
    "installable": True,
    "application": False,
    "license": "LGPL-3",
}


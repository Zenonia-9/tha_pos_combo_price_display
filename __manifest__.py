{
    "name": "POS Combo Price Display",
    "version": "17.0.1.0.2",
    "category": "Point of Sale",
    "summary": "Display the combo total on the parent and hide allocated component prices",
    "description": "Show a single combo total in the POS order line and standard receipt while preserving the underlying component prices and calculations.",
    "author": "Thein Htoo Aung",
    "license": "LGPL-3",
    "depends": ["point_of_sale"],
    "assets": {
        "point_of_sale._assets_pos": [
            "tha_pos_combo_price_display/static/src/js/combo_price_display.js",
            "tha_pos_combo_price_display/static/src/xml/combo_price_display.xml",
        ],
    },
    "installable": True,
    "application": False,
}

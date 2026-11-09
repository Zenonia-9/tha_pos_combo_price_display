# POS Combo Price Display

Odoo 17 addon that displays combo pricing clearly in Point of Sale.

## Features

- Shows the sum of allocated combo line prices on the combo parent.
- Hides allocated price, unit price, and discount details on combo components while retaining their names, quantities, and notes.
- Keeps standalone product prices unchanged.
- Applies to the shared POS order line widget used on the order screen and standard customer receipt.
- Changes display data only; it does not change order line prices, taxes, exports, inventory, or accounting.

## Setup

Install `tha_pos_combo_price_display` with `point_of_sale` installed. No configuration is required. Reload the POS after installation or upgrade.

The parent display uses the allocated component prices, including configured upgrades, with tax inclusion following the POS setting. It may differ from the combo product's configured base Sales Price.

## Scope

The addon ID and technical directory are `tha_pos_combo_price_display`; its display name is **POS Combo Price Display**. Custom receipt templates, kitchen printers, and other third-party POS interfaces may use separate templates and are outside this addon's scope.

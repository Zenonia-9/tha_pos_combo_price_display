# POS Combo Price Display for Odoo 17

For standard Odoo 17 `point_of_sale` POS/receipt components.

## What it does
- Shows the sum of the combo component amounts next to the combo parent.
- Hides the allocated price, unit price and discount of combo component lines.
- Still shows component names, quantities and notes.
- Keeps ordinary, standalone products' displayed prices unchanged.
- Uses the standard shared `point_of_sale.Orderline` widget, affecting both POS cart and standard customer receipt.
- Does not modify POS amounts, JSON exports, taxes, inventory, or accounting.

## Installation
1. Back up your database; test on staging first.
2. Extract the ZIP and place the `tha_pos_combo_price_display` directory under an Odoo custom addons path.
3. Ensure `addons_path` in odoo.conf contains the directory that **contains** this module.
4. Restart Odoo.
5. Apps > Update Apps List (developer mode), search for **POS Combo Price Display**, install.
6. Close and reopen your POS UI and hard-refresh your browser (Ctrl/Cmd+Shift+R).
7. Test a Double Set, standalone components, receipt reprint, refunds, tax configurations, and kitchen printers.

## Limitations and cautions
- This is a display-only module: accounting, backend order lines, invoices and back-office reports will still show the original allocated prices.
- The displayed parent combo price reflects the sum of actual allocated line prices including configured upgrades and, depending on the POS setting, taxes. It may differ from the configured base combo Sales Price.
- Hardware kitchen printers, restaurant bills, custom invoice reports or 3rd-party receipt templates may use their own templates and need separate updates.
- Test splitting bills, refunds, reloading saved orders and discounts before rolling out. Customized POS frontends may require template adjustments.
- This code was checked against the public Odoo 17 source structure; it has not been run in your specific instance.


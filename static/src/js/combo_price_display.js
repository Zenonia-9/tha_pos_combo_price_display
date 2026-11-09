/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { Orderline } from "@point_of_sale/app/store/models";

// Only override the data supplied to the shared POS/receipt order-line widget.
// Do not alter price_unit, tax, discount, JSON export, or payment calculations.
patch(Orderline.prototype, {
    getDisplayData() {
        const data = super.getDisplayData(...arguments);

        if (this.comboParent) {
            // Use a marker to suppress all price-related fragments in the template.
            // The original data and underlying order line remain unchanged.
            return { ...data, comboHiddenPrice: true };
        }

        if (this.comboLines?.length) {
            // Standard Odoo 17 has the parent line at zero and allocates the
            // combo value to its children. Show the *real* sum on the parent.
            const inclusive = this.pos.config.iface_tax_included === "total";
            const comboAmount = this.getAllLinesInCombo().reduce((total, line) => {
                const prices = line.get_all_prices();
                return total + (inclusive ? prices.priceWithTax : prices.priceWithoutTax);
            }, 0);
            return {
                ...data,
                price: this.env.utils.formatCurrency(comboAmount, this.currency),
                comboDisplayParent: true,
            };
        }
        return data;
    },
});

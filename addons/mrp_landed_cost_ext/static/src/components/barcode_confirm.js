/** @odoo-module **/
import { Component, useState } from "@odoo/owl";

export class FloorBarcodeConfirm extends Component {
    static template = "mrp_landed_cost_ext.FloorBarcodeConfirm";

    setup() {
        this.state = useState({ scannedLot: "", confirmed: false });
    }

    onScanLot(lotCode) {
        this.state.scannedLot = lotCode.trim();
        this.state.confirmed = Boolean(this.state.scannedLot);
    }
}

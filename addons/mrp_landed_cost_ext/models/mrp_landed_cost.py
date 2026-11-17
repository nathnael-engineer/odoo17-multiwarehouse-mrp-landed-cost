def allocate_landed_cost_by_weight(lines: list[dict], total_freight: float) -> list[dict]:
    """Allocate freight landed cost proportionally across picking lines by weight."""
    if total_freight < 0:
        raise ValueError("Freight cost cannot be negative.")
    total_weight = sum(item["weight_kg"] * item["qty"] for item in lines)
    if total_weight <= 0:
        raise ValueError("Total weight must exceed zero for weight-based allocation.")

    allocated = []
    running_sum = 0.0
    for idx, item in enumerate(lines):
        line_weight = item["weight_kg"] * item["qty"]
        if idx == len(lines) - 1:
            share = round(total_freight - running_sum, 2)
        else:
            share = round((line_weight / total_weight) * total_freight, 2)
            running_sum += share
        allocated.append({**item, "allocated_freight": share})
    return allocated


try:
    from odoo import api, fields, models

    class MrpProductionLandedExt(models.Model):
        _inherit = "mrp.production"

        landed_freight_total = fields.Monetary(
            string="Allocated Freight",
            currency_field="company_currency_id",
            readonly=True,
        )
        company_currency_id = fields.Many2one(
            related="company_id.currency_id",
            readonly=True,
        )
except ImportError:
    # Allows standalone unit testing outside an Odoo runtime container
    pass

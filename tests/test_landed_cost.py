from addons.mrp_landed_cost_ext.models.mrp_landed_cost import allocate_landed_cost_by_weight


def test_weight_based_freight_allocation_reconciles_to_cent():
    lines = [
        {"sku": "COMP-A", "qty": 10, "weight_kg": 2.5},
        {"sku": "COMP-B", "qty": 5, "weight_kg": 5.0},
        {"sku": "COMP-C", "qty": 2, "weight_kg": 12.5},
    ]
    result = allocate_landed_cost_by_weight(lines, total_freight=1000.00)
    assert round(sum(r["allocated_freight"] for r in result), 2) == 1000.00
    assert result[0]["allocated_freight"] == 333.33
    assert result[2]["allocated_freight"] == 333.34

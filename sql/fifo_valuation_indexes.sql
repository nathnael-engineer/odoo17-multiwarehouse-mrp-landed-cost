-- Composite partial index optimizing FIFO stock valuation layer queries on 2M+ rows
CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_svl_company_product_remaining
ON stock_valuation_layer (company_id, product_id, create_date)
WHERE remaining_qty > 0;

CREATE INDEX CONCURRENTLY IF NOT EXISTS idx_aml_journal_date_posted
ON account_move_line (company_id, account_id, date)
WHERE parent_state = 'posted';

#Source: https://stackoverflow.com/questions/75026826/attributeerror-tuple-object-has-no-attribute-symbol-when-downloading-stock
cursor.execute("""
    CREATE TABLE IF NOT EXISTS alpaca_stock_prices_1D (
        id INTEGER PRIMARY KEY,
        stock_id INTEGER,
        date NOT NULL,
        open NOT NULL,
        high NOT NULL,
        low NOT NULL,
        close NOT NULL,
        volume NOT NULL,
        CONSTRAINT fk_alpaca_stocks_list FOREIGN KEY (stock_id) REFERENCES alpaca_stocks_list (id)
        ON DELETE CASCADE
    )
""")
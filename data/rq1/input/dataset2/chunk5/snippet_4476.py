#Source: https://stackoverflow.com/questions/75026826/attributeerror-tuple-object-has-no-attribute-symbol-when-downloading-stock
# Define chunk of symbols to download with every server call.
symbols=['AMD', 'MSFT', 'NVDA', 'TOVX']
chunk_size = 2
for i in tqdm(range(0, len(symbols), chunk_size), desc='Downloading daily Data'):
    symbol_chunk = symbols[i:i + chunk_size]
    # Downloading 1D time-frame data...
    request_parameters = StockBarsRequest(
                    symbol_or_symbols=symbol_chunk,
                    timeframe=TimeFrame.Day,
                    start=datetime.strptime("2022-01-01", '%Y-%m-%d'),
                    end=None,
                    adjustment='raw'
             )
    daily_bars = client.get_stock_bars(request_parameters)
    for bar in daily_bars:
        stock_id = symbol_dic[bar.symbol]
        cursor.execute("""INSERT INTO alpaca_stock_prices_1D (stock_id, date, open, high, low, close, volume)
            VALUES (?, ?, ?, ?, ?, ?, ?)""",
                       (stock_id, bar.timestamp.date(), bar.open, bar.high, bar.low, bar.close, bar.volume))
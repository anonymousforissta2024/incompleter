#Source: https://stackoverflow.com/questions/43696005/attributeerror-module-pandas-has-no-attribute-read-csv-python3-5
# parser.py (built-in file in pandas) file has this implementation
read_csv = _make_parser_function('read_csv', sep=',')
read_csv = Appender(_read_csv_doc)(read_csv)
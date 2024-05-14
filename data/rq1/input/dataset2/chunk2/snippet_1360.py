#Source: https://stackoverflow.com/questions/74128016/quantstats-typeerror-invalid-comparison-between-dtype-datetime64ns-america
import quantstats as qs

qs.extend_pandas()

stock = qs.utils.download_returns('GLD')

qs.reports.html(stock, output='Output/GLD.html')
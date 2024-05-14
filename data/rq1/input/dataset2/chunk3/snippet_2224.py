#Source: https://stackoverflow.com/questions/65569574/beautifulsoup-initialization-type-error-trouble-troubleshooting
import pandas as pd
from PandasBasketball.stats import player_stats

dfs = [player_stats(requests.get(url), "per_minute") for url in full_player_urls[600:]]
all_stats = pd.concat(dfs)
all_stats[::500]
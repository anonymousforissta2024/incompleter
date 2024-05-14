#Source: https://stackoverflow.com/questions/57703538/typeerror-only-valid-with-datetimeindex-timedeltaindex-or-periodindex-but-got
weekly_summary["story_point"] = df.story_point.resample('W').sum()
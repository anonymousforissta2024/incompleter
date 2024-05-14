#Source: https://stackoverflow.com/questions/47718604/typeerror-during-datashader-aggregate-creation-between-python-3-5-and-3-6-enviro
agg = method(self.df[(self.df['time_position'] >= time_start) & (self.df['time_position'] <= time_end)
                                 | (self.df['time_position'].isnull())], x_field, y_field, ds.count_cat(agg_field))
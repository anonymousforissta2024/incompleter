#Source: https://stackoverflow.com/questions/49112402/typeerror-unsupported-operand-types-for-float-and-method
ratio_Production_Budget = abs((df_data['Production Budget'].mean() - df_data['Production Budget'].median()) / df_data['Production Budget'].median())
ratio_Worldwide_Gross = abs((df_data['Worldwide Gross'].mean() - df_data['Worldwide Gross'].median()) / df_data['Worldwide Gross'].median())
ratio_quarter = abs((df_data['quarter'].mean() - df_data['quarter'].median()) / df_data['quarter'].median())
ratio_duration = abs((df_data['duration'].mean() - df_data['duration'].median()) / df_data['duration'].median())
ratio_actor_1_facebook_likes = abs((df_data['actor_1_facebook_likes'].mean() - df_data['actor_1_facebook_likes'].median()) / df_data['actor_1_facebook_likes'].median())
ratio_imdb_score = abs((df_data['imdb_score'].mean() - df_data['imdb_score'].median()) / df_data['imdb_score'].median())
ratio_weekendTotal = abs((df_data['weekendTotal'].mean() - df_data['weekendTotal'].median()) / df_data['weekendTotal'].median)
ratio_midweekTotal = abs((df_data['midweekTotal'].mean() - df_data['midweekTotal'].median()) / df_data['midweekTotal'].median)

w1_mm = pd.Series(data= [ratio_Production_Budget, ration_Worldwide_Gross, ratio_quarter, ratio_duration, ratio_actor_1_facebook_likes, ratio_imdb_score, ratio_weekendTotal, ratio_midweekTotal],
                          index = ['Production Budget', 'Worldwide Gross', 'quarter', 'duration', 'actor_1_facebook_likes', 'imdb_score', 'weekendTotal', 'midweekTotal'])
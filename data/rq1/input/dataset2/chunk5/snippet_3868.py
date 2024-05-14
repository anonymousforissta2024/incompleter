#Source: https://stackoverflow.com/questions/62526457/attributeerror-series-object-has-no-attribute-df-hotel
perc_country_df_hotel = pd.DataFrame([df_hotel['country'].value_counts().df_hotel['country'].value_counts()*100/df_hotel.shape[0]]).T
perc_country_df_Hotel.columns = ['Count', '% Distribution']
perc_country_df_hotel

#then, 
df_hotel['country'].fillna('CountryWithBigPercentage', inplace= True)
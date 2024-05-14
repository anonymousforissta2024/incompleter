#Source: https://stackoverflow.com/questions/41320337/attributeerror-type-object-minimalfeatureextractionsettings-has-no-attribute
settings= MinimalFeatureExtractionSettings()

extracted_features = extract_features(df_to_extract, 
                                      column_id="id", 
                                      column_sort="time", 
                                      parallelization= 'per_kind', 
                                      feature_extraction_settings= settings)
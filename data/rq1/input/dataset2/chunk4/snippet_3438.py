#Source: https://stackoverflow.com/questions/66434981/styleframe-row-index-attributeerror-int-object-has-no-attribute-value
org_report = styleframe.StyleFrame.read_excel(f'{organisation.type}{TEMPLATE_SUFFIX}')
report_data = transform_aws_service_costs_to_excel_rows(organisation_costs)
report_data = pandas.DataFrame(report_data)

# Used to make sure the data concatenates properly.
report_data.columns = org_report.columns


org_report.data_df = concat([org_report.data_df.iloc[:4], report_data,
                             org_report.data_df.iloc[5:]], axis=0).reset_index(drop=True)

org_report.to_excel(create_report_name(organisation)).save() # Error occurs here.
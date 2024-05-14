#Source: https://stackoverflow.com/questions/59214111/how-to-resolve-attributeerror-when-trying-to-set-none-as-default-method-argument
import sa_reporting
from sa_body import *

dim_campaign_test = sa_reporting.saReport(
    body=dim_campaign_body,
    to_table='dimsa360CampaignTest',
    normalise=True,
    date_col=[4,5]
)
dim_campaign_test_download = dim_campaign_test.download_reports()
dim_campaign_test_download.load_to_db(sort_by=0) # THIS IS WHERE THE ERROR OCCURS
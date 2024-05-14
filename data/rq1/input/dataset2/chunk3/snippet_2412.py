#Source: https://stackoverflow.com/questions/57540372/typeerror-unhashable-type-numpy-ndarray-when-merging-pandas-datframes-from-b
from google.cloud import bigquery
from google.oauth2 import service_account
from google.cloud import bigquery_storage_v1beta1
from sklearn.model_selection import train_test_split
import pandas as pd

credentials = service_account.Credentials.from_service_account_file(
    'XXXXXXXXX.json')
project_id = 'XXXXXX'
client = bigquery.Client(credentials= credentials, project=project_id)

bqstorageclient = bigquery_storage_v1beta1.BigQueryStorageClient(
    credentials=credentials
)


language_query = """
  SELECT repo_name, Language, Bytes,
  CASE 
  when LOWER(Language) NOT IN ('javascript', 'python', 'ruby', 'java'
                        , 'php', 'c++', 'css', 'c#', 'go'
                        , 'c', 'typescript', 'shell', 'swift'
                        , 'scala', 'objective-c') then 'Other'
  else Language END AS language_category
  FROM github_project.langauges

  LIMIT 1000"""

language_query_dataframe = (
    client.query(language_query)
    .result()
    .to_dataframe(bqstorage_client=bqstorageclient)
)

commit_query = """
    SELECT Commit, Author, DateSeconds, repo_name
    FROM github_project.commits
    LIMIT 1000
    """

commit_query_dataframe = (
    client.query(commit_query)
    .result()
    .to_dataframe(bqstorage_client=bqstorageclient)
)

merged_data = pd.merge(commit_query_dataframe, language_query_dataframe, on='repo_name')
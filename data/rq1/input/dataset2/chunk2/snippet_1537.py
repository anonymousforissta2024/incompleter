#Source: https://stackoverflow.com/questions/75359017/filenotfounderror-errno-2-no-such-file-or-directory-while-exporting-a-parque
import mysql.connector
import pandas as pd
from google.cloud import storage
from datetime import datetime, timedelta
import os

def extract_data_to_gcs(request):
    connection = mysql.connector.connect(
        host=os.getenv('..'),
        user=os.getenv('...'),
        password=os.getenv('...'),
        database='....'
    )

    cursor = connection.cursor(buffered=True)

    tables = ["table1", "table2", "table3"]
    client = storage.Client()
    bucket = client.bucket('data-lake-archive')

    # Create a timestamp-based folder name
    now = datetime.now()
    folder_name = now.strftime("new_folder_%Y%m%d_%H%M%S")
    folder_path = f"{folder_name}/"

    # Create the folder in the GCS bucket
    blob = bucket.blob(folder_path)
    blob.upload_from_string("", content_type="application/octet-stream")

    for table in tables:
        cursor.execute("SELECT * FROM {}".format(table))
        chunks = pd.read_sql_query("SELECT * FROM {}".format(table), connection, chunksize=5000000)
        for i, chunk in enumerate(chunks):
            chunk.columns = [str(col) for col in chunk.columns]
            ingestion_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            parquet_file_path = folder_path + f"{table}-{i}.parquet"
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            # parquet_file_path = folder_path + f'abc.parquet'
            print(f'folder path is {folder_path}')
            print(f'parquet file path is {parquet_file_path}')
            chunk.to_parquet(parquet_file_path, engine='fastparquet', compression='snappy')
            # blob = bucket.blob(folder_path + f'{table}-{i}.parquet')
            # blob.upload_from_filename(folder_path + f'{table}-{i}.parquet')

        cursor.execute("SELECT table_name, column_name FROM information_schema.key_column_usage WHERE referenced_table_name = '{}'".format(table))
        referenced_tables = cursor.fetchall()
        for referenced_table in referenced_tables:
            chunks = pd.read_sql_query("SELECT * FROM {}".format(referenced_table[0]), connection, chunksize=5000000)
            for i, chunk in enumerate(chunks):
                chunk.columns = [str(col) for col in chunk.columns]
                ingestion_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                chunk.to_parquet(f"{folder_path}{referenced_table[0]}-{ingestion_timestamp}-{i}.parquet", engine='fastparquet', compression='snappy')
                blob = bucket.blob(folder_path + f'{referenced_table[0]}-{ingestion_timestamp}-{i}.parquet')
                blob.upload_from_filename(folder_path + f'{referenced_table[0]}-{ingestion_timestamp}-{i}.parquet')

    return 'Data extracted and uploaded to GCS'
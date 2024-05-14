#Source: https://stackoverflow.com/questions/77711881/typeerrorunsupported-data-type-class-deltalake-table-deltatablehow-to-upl
from azure.storage.blob import BlobServiceClient
import pandas as pd
import json
from deltalake.writer import write_deltalake
from deltalake import write_deltalake, DeltaTable

import asyncio
import ast
from azure.eventhub.aio import EventHubConsumerClient

BLOB_CONTAINER_NAME = "iot"
EVENT_HUB_CONNECTION_STR = "Endpoint=sb://dhbchisdbc.servicebus.windows.net/;SharedAccessKeyName=iothubowner;SharedAccessKey=fsdojfosdjf=;EntityPath=iothub-ehub-iothubfree-kcnk-b6c03da7fe"
EVENT_HUB_NAME = "iothub-ehub-iothubfree-cdhscb-jcnj"
BLOB_STORAGE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName='dygsgcsd';AccountKey=kdncs+dncsdhncs+AStVSl3cg==;EndpointSuffix=core.windows.net"


async def on_event(partition_context, event):
    data=ast.literal_eval(event.body_as_str(encoding="UTF-8"))
    frame=pd.DataFrame.from_dict(data, orient='index')
    #write to delta format
    write_deltalake('/delta/newtable', frame,mode='append')
    # reading to delta format
    dt = DeltaTable('/delta/newtable')
   
    blob_service_client = BlobServiceClient.from_connection_string(BLOB_STORAGE_CONNECTION_STRING)
    blob_path_admin = f'/newPath'
    blob_client_admin = blob_service_client.get_blob_client(container=BLOB_CONTAINER_NAME, blob=blob_path_admin)
    blob_client = blob_client_admin.upload_blob(data=dt, overwrite=True)

    await partition_context.update_checkpoint(event)

async def main():

    client = EventHubConsumerClient.from_connection_string(
        EVENT_HUB_CONNECTION_STR,
        consumer_group="$Default",
        eventhub_name=EVENT_HUB_NAME,
    )
    async with client:
        await client.receive(on_event=on_event, starting_position="-1")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
#Source: https://stackoverflow.com/questions/76857472/attributeerror-prototype-object-has-no-attribute-descriptor-while-running
def convert_to_pubsub_message(element):
 if element is None:
    return None
 pubsub_data = {"table": element["table"], "payload": element["values"]}
 pubsub_message = {
    "data": json.dumps(pubsub_data).encode("utf-8"),
    "attributes": {}
 }
 print("Pub/Sub Message:", pubsub_message)
 return pubsub_message

with beam.Pipeline(options=options) as p:
# Read the JSON records from GCS or any source
  records = p | "Read JSON records" >> beam.io.ReadFromText(gcs_json_file)
  # Extract payload and table name from each record
  extracted_data = (
    records
    | "Extract Payload and Table" >> beam.ParDo(ExtractPayloadAndTable())
  )
  # Send extracted payloads to Pub/Sub
  message = (
    extracted_data
    | "Convert to Pub/Sub Message" >> beam.Map(convert_to_pubsub_message)
    | "Send Payload to Pub/Sub" >> WriteToPubSub(topic=pubsub_topic)
  )
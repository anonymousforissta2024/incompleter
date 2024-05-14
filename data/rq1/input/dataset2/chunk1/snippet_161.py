#Source: https://stackoverflow.com/questions/57722270/getting-typeerror-unhashable-type-dict-while-doing-bulk-upload-in-elastics
temp_entities_list = []
for each_row in master_entities:
    entity_data = {}
    entity_data['entity_id'] = each_row.id
    entity_data['createdat'] = each_row.createdat
    entity_data['updatedat'] = each_row.updatedat
    entity_data['individual_business_tag']=each_row.individual_business_tag
    temp_entities_list.append(entity_data)

def indexing(entity_list):
    for entity in entity_list:
        index_name = "demo"
        yield{
            "_index":index_name,
            "_type":"businesses",
            "_source" :{
                "body":entity
            }
        }
try:
    helpers.bulk(es,testing(temp_entities_list))
except Exception as exe:
    indexing_logger.exception("Error:"+str(exe))
#Source: https://stackoverflow.com/questions/74770489/i-am-trying-to-add-the-tag-freefrom-tag-for-particular-compute-instances-in-oc
core_client = oci.core.compute_client.ComputeClient(config)
core_client.base_client.set_region('us-phoenix-1')
vol=oci.core.BlockstorageClient(config)
# Send the request to service, there are more available parameters to send in the request
lista = core_client.list_instances(compartment_id=compartment_id,lifecycle_state="STOPPED")

for i in lista.data:
    inst=core_client.get_instance(instance_id=i.id)
    #print(inst.data)
    update_volume_response = core_client.update_instance(update_instance_details = oci.core.models.UpdateInstanceDetails(freefrom_tag={"shutdown": "no"}))
    print(update_volume_response) 
    break
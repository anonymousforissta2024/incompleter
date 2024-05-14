#Source: https://stackoverflow.com/questions/74878801/attributeerror-dict-object-has-no-attribute-instance-python
def status_ec2_instance(instanceIds_list, region_Name):
    ec2 = boto3.resource('ec2', region_name=region_Name)
    ec2_client = boto3.client('ec2', region_name=region_Name)
    print(instanceIds_list)
    a=instanceIds_list[0]
    print(a)
    #response=ec2_client.describe_instances(InstanceIds=instanceIds_list)
    response = ec2_client.describe_instances(Filters=[
        {
            'Name': 'private-ip-address',
            'Values': [
                a,
            ]    
        }
    ])
    for ec2 in response['Reservations'][0]['Instances']:
        instanceIds = ec2['InstanceId']
        print(instanceIds)
        response=ec2_client.start_instances(InstanceIds=[instanceIds])
        print('started your instances: ' + str(instanceIds))
        instance_started = []
        print(instanceIds)
        instance_response = ec2.Instance([instanceIds])
        instance_state = instance_response.state
        if instance_state['Name'] == 'running'and instance not in instance_started:
            instance_started.append(instance)
            print(instance,instance_state['Name'])
                
                    
    print("started instances ",str(instance_started))
    return instance_started

if __name__ == "__main__":
    PrivateIP = sys.argv[1]
    region_Name = "us-east-1"
    #instanceIds_list = [instanceIds]
    instanceIds_list = [PrivateIP]
    status_list=status_ec2_instance(instanceIds_list, region_Name)
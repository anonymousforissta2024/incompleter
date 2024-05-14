#Source: https://stackoverflow.com/questions/76185529/it-keeps-given-the-error-attributeerror-nonetype-object-has-no-attribute-get
import boto3
InstanceIds = ['I-1234', 'I-2345', 'I-6789']
ec2 = boto3.resource('ec2')
for inst in InstanceIds:
    instance_response = ec2.Instance(inst)
    if instance_response is None:
        print(instance_response, " has a value of None")
    else:
        instance_tags = instance_response.tags
        for item in instance_tags:
            if item['Key'] == 'Environment':
                val = item['Value']
        pattern = re.compile(r'\bpr\w*', re.IGNORECASE)
        matches = pattern.findall(val)
        if matches:
            print("Prod Tag exists in ", inst, val)
        else:
            nonPRD_tags_exists_instances.append(inst)
            print("Prod Tag doesn't exists in ", inst, val) 
print(nonPRD_tags_exists_instances) 
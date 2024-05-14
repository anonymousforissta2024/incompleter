#Source: https://stackoverflow.com/questions/57871615/boto3-get-tenancy-value-from-placement-gives-name-error
for i in client.instances.all():
    for n in i.placement:
        if 'tenancy' in n['Key']:
            tenancy = n['Value']
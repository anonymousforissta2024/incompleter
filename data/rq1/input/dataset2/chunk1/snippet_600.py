#Source: https://stackoverflow.com/questions/51946150/django-typeerror-not-supported-between-instances-model-objects
if (dev_filter!="") and (dev_filter!="-1"):
    device_list = Device.objects.all().filter(device_model = dev_filter)
else:
    device_list = Device.objects.all()

dev_status_list = []
for dev in device_list:
    try:
        dev_status_list.append(DeviceTest.objects.filter(device_id=dev.pk).latest('created_at').status)
    except:
        dev_status_list.append("Not checked")

device_list = [device_list for (dev_status_list, device_list) in sorted(zip(dev_status_list, device_list))]

if (order == '-'):
    device_list.reverse()
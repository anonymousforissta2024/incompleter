#Source: https://stackoverflow.com/questions/75402627/how-to-handle-python-typeerror-nonetype-object-is-not-subscriptable-on-dict-valu
sites_response =requests.request("GET", url_dcim_sites, headers=headers, data=payload)

sites_json = sites_response.json()

sites_results = sites_json['results']

for site in sites_results:
  id_number = site['id']
  name = site['name']
  region_name = site['region']['name']
  status = site['status']['value']
  #print(f"ID:{id_number:5} | Hostname:{hostname:20} | IP Address:{ipaddr!s:12} | Site:{site_id:5}") 
  sites = dict(ID=id_number, Name=name, Region=region_name, Status=status)
  format_sites = f"ID: {sites['ID']:5} | Name: {sites['Name']:20} | Region: {sites['Region']:10} | Status: {sites['Status']:5}"
  print(format_sites)
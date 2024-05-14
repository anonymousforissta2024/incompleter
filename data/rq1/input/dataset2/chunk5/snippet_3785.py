#Source: https://stackoverflow.com/questions/60345611/dont-understand-cause-of-this-typeerror-exception
cc_gdps = {}
for gdp_dict  in gdp_data:
    if gdp_dict['Year'] == 2014:
        country_name = gdp_data["Country Name"]
        gdp = int(float(gdp_data['Value']))
        code = get_country_code(country_name)
    if code:
        cc_gdps[code] = gdp
#Group the countries into 3 gdp level
cc_gdps_1,cc_gdps_2,cc_gdps_3 = {},{},{}
for cc,gdp in cc_gdps.items():
    if gdp < 5000000000:
        cc_gdps_1[cc]=round(gdp/1000000000)
    elif gdp < 5000000000:
        cc_gdps_2[cc] = round(gdp/1000000000)
    else:
        cc_gdps_3[cc] = round(gdp/1000000000)
#see how many countries are in each level
print(len(cc_gdps_1),len(cc_gdps_2),len(cc_gdps_3))
wm_style = RC('#336699',base_style=LCS)
wm = World(style = wm_style)
wm.title = 'Global GDP in 2014, by country.'
wm.add('0-5bln',cc_gdps_1)
wm.add('5bln-50bln',cc_gdps_2)
wm.add('>50bln', cc_gdps_3)
wm.render_to_file('global_gdp.svg')
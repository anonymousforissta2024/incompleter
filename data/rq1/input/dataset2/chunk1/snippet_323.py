#Source: https://stackoverflow.com/questions/55735777/typeerror-not-supported-between-instances-of-str-and-int-in-version-num
from distutils.version import LooseVersion
versions_list = ['2.5.6.RC02', '2.0.8', '2.0-m2']
versions_list.sort(key=LooseVersion, reverse=False)

print(versions_list) 
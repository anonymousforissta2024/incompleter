import pkg_resources
installed_packages = pkg_resources.working_set
for m in installed_packages_list:
    print(m)
#Source: https://stackoverflow.com/questions/61902310/typeerror-init-got-an-unexpected-keyword-argument-num-workers
from nornir import InitNornir
nr = InitNornir(config_file="C:/Users/<REMOVED>/Desktop/config.yaml")
nr.filter(site="uk").inventory.hosts.keys()
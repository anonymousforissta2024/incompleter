#Source: https://stackoverflow.com/questions/61902310/typeerror-init-got-an-unexpected-keyword-argument-num-workers
from nornir import InitNornir
nr = InitNornir(
    core={"num_workers": 100},
    inventory={
        "plugin": "nornir.plugins.inventory.simple.SimpleInventory",
        "options": {
            "host_file": "inventory/hosts.yaml",
            "group_file": "inventory/groups.yaml"
        }
    }
)
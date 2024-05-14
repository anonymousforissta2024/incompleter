#Source: https://stackoverflow.com/questions/54274442/module-imported-in-one-function-nameerror-in-another-function-called-afterward
#!/usr/bin/python3

import importlib.util
from subprocess import Popen, PIPE, STDOUT
import sys
import subprocess
import time


accessToken                 = 'ABC'
dropletName                 = 'newDropletAndTag'
tagName                     = dropletName

def Install():
    pass
    #This function installs the package and other things if they are not already present. 


def CreateDroplet():
    newDroplet = digitalocean.Droplet(  token       = accessToken, 
                                        name        = dropletName,
                                        region      = 'NYC1',
                                        image       = 'ubuntu-16-04-x64',
                                        size_slug   = 's-1vcpu-1gb',
                                        ssh_keys    = sshKeysList, 
                                        backups     = False
                                        )    

def Run():
    import digitalocean
    myManager = digitalocean.Manager(token=accessToken)
    myDroplets = myManager.get_all_droplets(tag_name=tagName)

    Install() 
    CreateDroplet()


def Main():
    #START OF SCRIPT
    print('\n\n\n')
    print('---- Start Of Script ----')
    Run()
    print('---- End Of Script ----')
    print('\n\n\n')
    #END OF SCRIPT
if __name__ == '__main__':
    Main()
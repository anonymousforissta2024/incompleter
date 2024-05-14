#Source: https://stackoverflow.com/questions/70197401/azure-function-attributeerror-subscriptionclient-object-has-no-attribute-su
import logging

import subprocess
import json
import os
from azure.cli.core import get_default_cli
from azure.mgmt.containerservice import ContainerServiceClient
from azure.identity import ClientSecretCredential
from azure.mgmt.subscription import SubscriptionClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.containerservice.models import (ManagedClusterAgentPoolProfile, ManagedCluster)

def main(env: str) -> str:
    logging.info('Python aks-upgrade function processed a request.')
    #print("Environment:", env)
    if env:
      try:
        credential = ClientSecretCredential(
          tenant_id='mytenantid',
          client_id = os.environ["function_client_id"],  
          client_secret= os.environ["function_client_secret"]
        )
        
        sub_client = SubscriptionClient(credential=credential)
      except:
        print("An exception occurred")
        #sub_client.subscriptions.list()
      print("Listing Subscriptions....")
      for sub in sub_client.subscriptions.list():   
            print("Sub_Name:", sub.display_name, "Environment:", env)
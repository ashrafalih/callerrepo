import os
import requests
import sys

TOKEN = str(sys.argv[1])
OWNER = str(sys.argv[2])
REPO = str(sys.argv[3])
Workflow_Name = str(sys.argv[4])
parameter1 = str(sys.argv[5])
parameter2 = str(sys.argv[6])

print("The token value is")

def trigger_workflow(workflow_name, parameter1, parameter2):
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "Authorization": f"token {TOKEN}",
    }

    data = {
        "event_type": Workflow_Name,  
        "client_payload": {  # this is the way to get the values in workflow1 to workflow2
            'parameter1': parameter1,
            'parameter2': parameter2  
        }
    }

    # using the request module and invoking the post method and constructing the API
    responseValue = requests.post(f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches", json=data, headers=headers)
    print(responseValue.content)
    # responseValue = requests.post(f"https://api.github.com/repos/{OWNER}/{REPO}/dispatches", json=data, headers=headers)
    print("The response message is ", responseValue.content)  

trigger_workflow(Workflow_Name, parameter1, parameter2) 

import requests
import json
requests.packages.urllib3.disable_warnings()
endpoint = "https://api.ciscospark.com/v1"
resource ="/people"
access_token = "ZGVmZGFkNWItN2IxMS00NGUzLWE2MWUtNmRlZjcyNDg2YmM0ZDg2MWU3NWUtMGRm_PF84_0fbd1c6c-a47c-483e-98db-c53aeefc4680"
headers = {
             "content-type" : "application/json",
             "authorization" : "Bearer " + access_token
         }
param = "?email=antonia.andreica.m@gmail.com"
url = endpoint+resource+param
response = requests.get(url, headers=headers, verify=False).json()


person = response["items"][0]
print('Name: ' + person['displayName'])
print('Email: ' + person['emails'][0])
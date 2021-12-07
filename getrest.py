import requests 

apiUrl = "https://api.ciscospark.com/v1/rooms"
access_token = "ZGVmZGFkNWItN2IxMS00NGUzLWE2MWUtNmRlZjcyNDg2YmM0ZDg2MWU3NWUtMGRm_PF84_0fbd1c6c-a47c-483e-98db-c53aeefc4680"

httpHeaders = {"Content-type" : "application/json", "Authorization" : "Bearer " + access_token}
queryParams = {"sortBy" : "lastactivity", "max" : "2"}
response = requests.get(url=apiUrl, headers=httpHeaders, params=queryParams)

print(response.status_code)
print(response.text)



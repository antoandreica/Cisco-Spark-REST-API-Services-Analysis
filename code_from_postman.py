import requests
url = "https://api.ciscospark.com/v1/rooms"

payload = {}
headers = {
  'Authorization': 'Bearer ZGVmZGFkNWItN2IxMS00NGUzLWE2MWUtNmRlZjcyNDg2YmM0ZDg2MWU3NWUtMGRm_PF84_0fbd1c6c-a47c-483e-98db-c53aeefc4680'
}

response = requests.request("GET", url, headers=headers, data = payload)

print(response.text.encode('utf8'))

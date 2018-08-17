import requests
url='https://sandboxapicem.cisco.com/'
response=requests.get(url,verify=False)
print(response)
user='devnetuser'
password='Cisco123!'
r=requests.get(url,auth=(user,password))
r.status_code
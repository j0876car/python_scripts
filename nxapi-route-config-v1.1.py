import requests 
import json  
url='http://10.3.198.100/ins'
switchuser='admin'
switchpassword='Password'

myheaders={'content-type':'application/json-rpc'}
payload=[
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "vrf context management",
      "version": 1
    },
    "id": 1
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "ip route 192.168.255.0/24 10.3.198.130",
      "version": 1
    },
    "id": 2
  },
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "copy run start",
      "version": 1
    },
    "id": 3
  }
 ]
#response = requests.post(url,data=json.dumps(payload),headers=myheaders,auth=(switchuser,switchpassword)).json()
#response = requests.request("POST",url,data=json.dumps(payload),headers=myheaders,auth=(switchuser,switchpassword)).json()
response = requests.post(url,data=json.dumps(payload),headers=myheaders,auth=(switchuser,switchpassword))
json_response = response.json()
#print(response.status_code)
print(response.text)

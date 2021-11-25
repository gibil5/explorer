"""
Explore endpoints with Requests library

"""
import requests 
import my_token
import funcs


endpoints = [
  #"https://dev.zengrc.com/health",

  # API-DEVICES
  #("api-devices", "https://devices-staging.electric.ai/staging"),
  #("api-devices", "https://devices-staging.electric.ai/staging/v2/devices"),
  #("api-devices", "https://devices-staging.electric.ai/staging/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7"),
  #("api-devices", "http://localhost:3000/local/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7"),
  #("api-devices", "http://localhost:3000/local/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7&assigned_to=4b74a197-09f6-4347-8ed7-5f8ff5165139"),
  #("api-devices", "http://localhost:3000/local/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7&assignedTo=4b74a197-09f6-4347-8ed7-5f8ff5165139"),

  # API-ORGANIZATIONS
  ("api-organizations", "customers", "http://localhost:3000/customers"),
  #("api-organizations", "employees", "http://localhost:3000/employees/search?term=patricia60@herrera.biz"),
  #("api-organizations", "offices", "http://localhost:3000/offices/0c63dcc9-dc4d-4287-87d8-dc752599a2b1"),
 ]


healthy_status = 200

token = my_token.get_token()

#data = {"ip": "1.1.2.3"}
#data = {"customerId": "9a919a42-b506-49ee-b053-402827b761b7"}
data = {}

#headers = {}
headers = {"Authorization": "Bearer " + token}

for ep in endpoints: 
    api = ep[0]
    entity = ep[1]
    url = ep[2]

    print('\nEndpoint: ', url)
    print('API: ', api)
    print('Entity: ', entity)
    print('GET\n')

    try: 
        r = requests.get(url, data=data, headers=headers)
        print(r)
        print()
        #print(r.content)
        #print()
        #print(r.headers['content-type'])
        #print()
        #print(r.encoding)
        #print()
        #print(r.text)
        #print()
        #print(r.json())
        #print()

        if api == "api-devices":
            funcs.decode_api_devices(r)

        if api == "api-organizations":
            funcs.decode_api_organizations(r, entity)

        print(r.status_code)
        print('Server OK\n')

    except: 
        print('Error !')
        print('Impossible to connect')

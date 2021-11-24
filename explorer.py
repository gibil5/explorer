"""
Exploring our Endpoints with requests

Get devices
-------------------
http://localhost:3000/local/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7
http://localhost:3000/local/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7&assigned_to=4b74a197-09f6-4347-8ed7-5f8ff5165139

Create devices
-------------------
python3 devices.py seed --stage local --partition 9a919a42-b506-49ee-b053-402827b761b7 --macs 3 --windows 5
python3 devices.py seed --stage local --partition 9a919a42-b506-49ee-b053-402827b761b7 --macs 3

Assign devices
-------------------
http://localhost:3000/local/v2/devices/:hostIdentifier/assignment



"assigned_to":
"assigned_by":
"email": "javier.revilla@electric.ai",
"id": "4b74a197-09f6-4347-8ed7-5f8ff5165139",

"id": "1b940372-8044-4de8-a326-f62fe0952767",
"email": "caitlin.griffin@electric.ai",

hostIdentifier
9a919a42-b506-49ee-b053-402827b761b7::0b4014c238cf79ab35bf95ee35f46b20
9a919a42-b506-49ee-b053-402827b761b7::55a47c8b40162bbb9c82fe23fe8dd0ca
9a919a42-b506-49ee-b053-402827b761b7::77b38a4e9ef8d5738fda8d9e0f461f63

"""
import requests 
import my_token


endpoints = [
  #"https://dev.zengrc.com/health",
  #"https://devices-staging.electric.ai/staging",
  #"https://devices-staging.electric.ai/staging/v2/devices",
  "https://devices-staging.electric.ai/staging/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7",

  #"http://localhost:3000/local/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7",
  #"http://localhost:3000/local/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7&assigned_to=4b74a197-09f6-4347-8ed7-5f8ff5165139",
  #"http://localhost:3000/local/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7&assignedTo=4b74a197-09f6-4347-8ed7-5f8ff5165139",
 ]

#ep = "https://devices-staging.electric.ai/staging/v2/devices?customerId=9a919a42-b506-49ee-b053-402827b761b7"

healthy_status = 200

#token = ''
#token = 'MYREALLYLONGTOKENIGOT'


#token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6RXhNVEE0TWpOQlF6RXdRek14TURVeFJETTFNMEZDTlRCR05FSkRORUZGTVRsRlFqVTBNUSJ9.eyJodHRwczovL2FwcC5lbGVjdHJpYy5haS9zY29wZXMiOlsiZ2xvYmFsLmN1c3RvbWVyczpyZWFkIiwiZ2xvYmFsLmN1c3RvbWVyczp3cml0ZSIsImdsb2JhbC51c2VyczpyZWFkIiwiZ2xvYmFsLnVzZXJzOndyaXRlIl0sImlzcyI6Imh0dHBzOi8vZWxlY3RyaWMtc3RhZ2luZy5hdXRoMC5jb20vIiwic3ViIjoiSmRVb2ZaUFNOcDQxOERxOE1lSElrZTVrWnBQYVpZNjBAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZWxlY3RyaWMtc3RhZ2luZy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTYzNzc5NjEyMywiZXhwIjoxNjM3ODgyNTIzLCJhenAiOiJKZFVvZlpQU05wNDE4RHE4TWVISWtlNWtacFBhWlk2MCIsInNjb3BlIjoicmVhZDpjbGllbnRfZ3JhbnRzIGNyZWF0ZTpjbGllbnRfZ3JhbnRzIGRlbGV0ZTpjbGllbnRfZ3JhbnRzIHVwZGF0ZTpjbGllbnRfZ3JhbnRzIHJlYWQ6dXNlcnMgdXBkYXRlOnVzZXJzIGRlbGV0ZTp1c2VycyBjcmVhdGU6dXNlcnMgcmVhZDp1c2Vyc19hcHBfbWV0YWRhdGEgdXBkYXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBkZWxldGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgcmVhZDp1c2VyX2N1c3RvbV9ibG9ja3MgY3JlYXRlOnVzZXJfY3VzdG9tX2Jsb2NrcyBkZWxldGU6dXNlcl9jdXN0b21fYmxvY2tzIGNyZWF0ZTp1c2VyX3RpY2tldHMgcmVhZDpjbGllbnRzIHVwZGF0ZTpjbGllbnRzIGRlbGV0ZTpjbGllbnRzIGNyZWF0ZTpjbGllbnRzIHJlYWQ6Y2xpZW50X2tleXMgdXBkYXRlOmNsaWVudF9rZXlzIGRlbGV0ZTpjbGllbnRfa2V5cyBjcmVhdGU6Y2xpZW50X2tleXMgcmVhZDpjb25uZWN0aW9ucyB1cGRhdGU6Y29ubmVjdGlvbnMgZGVsZXRlOmNvbm5lY3Rpb25zIGNyZWF0ZTpjb25uZWN0aW9ucyByZWFkOnJlc291cmNlX3NlcnZlcnMgdXBkYXRlOnJlc291cmNlX3NlcnZlcnMgZGVsZXRlOnJlc291cmNlX3NlcnZlcnMgY3JlYXRlOnJlc291cmNlX3NlcnZlcnMgcmVhZDpkZXZpY2VfY3JlZGVudGlhbHMgdXBkYXRlOmRldmljZV9jcmVkZW50aWFscyBkZWxldGU6ZGV2aWNlX2NyZWRlbnRpYWxzIGNyZWF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgcmVhZDpydWxlcyB1cGRhdGU6cnVsZXMgZGVsZXRlOnJ1bGVzIGNyZWF0ZTpydWxlcyByZWFkOnJ1bGVzX2NvbmZpZ3MgdXBkYXRlOnJ1bGVzX2NvbmZpZ3MgZGVsZXRlOnJ1bGVzX2NvbmZpZ3MgcmVhZDpob29rcyB1cGRhdGU6aG9va3MgZGVsZXRlOmhvb2tzIGNyZWF0ZTpob29rcyByZWFkOmVtYWlsX3Byb3ZpZGVyIHVwZGF0ZTplbWFpbF9wcm92aWRlciBkZWxldGU6ZW1haWxfcHJvdmlkZXIgY3JlYXRlOmVtYWlsX3Byb3ZpZGVyIGJsYWNrbGlzdDp0b2tlbnMgcmVhZDpzdGF0cyByZWFkOnRlbmFudF9zZXR0aW5ncyB1cGRhdGU6dGVuYW50X3NldHRpbmdzIHJlYWQ6bG9ncyByZWFkOnNoaWVsZHMgY3JlYXRlOnNoaWVsZHMgdXBkYXRlOnNoaWVsZHMgZGVsZXRlOnNoaWVsZHMgcmVhZDphbm9tYWx5X2Jsb2NrcyBkZWxldGU6YW5vbWFseV9ibG9ja3MgdXBkYXRlOnRyaWdnZXJzIHJlYWQ6dHJpZ2dlcnMgcmVhZDpncmFudHMgZGVsZXRlOmdyYW50cyByZWFkOmd1YXJkaWFuX2ZhY3RvcnMgdXBkYXRlOmd1YXJkaWFuX2ZhY3RvcnMgcmVhZDpndWFyZGlhbl9lbnJvbGxtZW50cyBkZWxldGU6Z3VhcmRpYW5fZW5yb2xsbWVudHMgY3JlYXRlOmd1YXJkaWFuX2Vucm9sbG1lbnRfdGlja2V0cyByZWFkOnVzZXJfaWRwX3Rva2VucyBjcmVhdGU6cGFzc3dvcmRzX2NoZWNraW5nX2pvYiBkZWxldGU6cGFzc3dvcmRzX2NoZWNraW5nX2pvYiByZWFkOmN1c3RvbV9kb21haW5zIGRlbGV0ZTpjdXN0b21fZG9tYWlucyBjcmVhdGU6Y3VzdG9tX2RvbWFpbnMgdXBkYXRlOmN1c3RvbV9kb21haW5zIHJlYWQ6ZW1haWxfdGVtcGxhdGVzIGNyZWF0ZTplbWFpbF90ZW1wbGF0ZXMgdXBkYXRlOmVtYWlsX3RlbXBsYXRlcyByZWFkOm1mYV9wb2xpY2llcyB1cGRhdGU6bWZhX3BvbGljaWVzIHJlYWQ6cm9sZXMgY3JlYXRlOnJvbGVzIGRlbGV0ZTpyb2xlcyB1cGRhdGU6cm9sZXMgcmVhZDpwcm9tcHRzIHVwZGF0ZTpwcm9tcHRzIHJlYWQ6YnJhbmRpbmcgdXBkYXRlOmJyYW5kaW5nIHJlYWQ6bG9nX3N0cmVhbXMgY3JlYXRlOmxvZ19zdHJlYW1zIGRlbGV0ZTpsb2dfc3RyZWFtcyB1cGRhdGU6bG9nX3N0cmVhbXMgY3JlYXRlOnNpZ25pbmdfa2V5cyByZWFkOnNpZ25pbmdfa2V5cyB1cGRhdGU6c2lnbmluZ19rZXlzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.vBuS8xPA3yscq0Enx6XBnXJKH29se2rqYzNN-Y7j0FEJcwORdCv2Pc-i6FCngXZpG5-jG_7Si1hOVH427V4YkFCZZlk1YdIBd07Iyeh4QaZ9bZcYU5u9JfxOmh-uqTkp59HmnURRmifP_onjb0Q1Pfpj1j5o5m6-z1H_9pLTTZbxaSTuNyouqr_STXQKs_p_F0lJoVt95J5GVF0CSPpvUkCNU2LGXvPNsALPBFpCN0UApJrIrrCbulziMgAZN5N3BVCPIsfm0-W7vo9CjAt4awARLIIX_PMwmfSNAZ-ggpEsNPwgf0EiCukspqqFuP01Hw_z4roZ3YafeqDZd-ZW8w'

token = my_token.get_token()

#data = {"ip": "1.1.2.3"}
data = {}
#data = {"customerId": "9a919a42-b506-49ee-b053-402827b761b7"}

headers = {"Authorization": "Bearer " + token}
#headers = {}

for url in endpoints: 

    print('\nEndpoint: ', url)
    print('GET\n')

    try: 
        #r = requests.get(url)
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


        data_json = r.json()['data']
        print(data_json)

        idx = 0
        for d in data_json:

            #if d['assigned']:
            if True:
                print(idx)
                #print(d)
                #print()
                print(d['assigned'])
                print('assigned_to:\t', d['assigned_to'])
                #print(d['customer_id'])
                print('host_identifier:', d['host_identifier'])
                print(d['hostname'])
                print(d['username'])
                print()
            idx += 1
        print()
        print('after:', r.json()['after'])
        print('count:', r.json()['count'])
        print('total:', r.json()['total'])


        print()
        print(r.status_code)
        print('Server OK\n')

    except: 
        print('Error !')
        print('Impossible to connect')

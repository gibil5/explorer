"""
Prepare for Testing
"""
import requests 

#endpoints = [
#  "http://localhost:3000/local/v2/devices/9a919a42-b506-49ee-b053-402827b761b7::0b4014c238cf79ab35bf95ee35f46b20/assignment"
#]

ep_0 = "http://localhost:3000/local/v2/devices/"
ep_1 = "/assignment"

hosts = [
    #"9a919a42-b506-49ee-b053-402827b761b7::0b4014c238cf79ab35bf95ee35f46b20",
    #"9a919a42-b506-49ee-b053-402827b761b7::55a47c8b40162bbb9c82fe23fe8dd0ca",
    #"9a919a42-b506-49ee-b053-402827b761b7::77b38a4e9ef8d5738fda8d9e0f461f63",

    #"9a919a42-b506-49ee-b053-402827b761b7::8c22d5b7c97b2a834cdacb153e4b9183",
    #"9a919a42-b506-49ee-b053-402827b761b7::423d016e1f3a8e148cde2a43dd5d7658",
    #"9a919a42-b506-49ee-b053-402827b761b7::5b4f3f9cb086458c85edbc6b4d0b085d",

    #"9a919a42-b506-49ee-b053-402827b761b7::78acce143547d313e627bb84cafc4cb0", 
    #"9a919a42-b506-49ee-b053-402827b761b7::312e7b4b39f9e4e1217451e7a8389047", 
    #"9a919a42-b506-49ee-b053-402827b761b7::751253bf92ae4d99420f9a83ca3133c1", 

    #"78acce143547d313e627bb84cafc4cb0", 
    #"312e7b4b39f9e4e1217451e7a8389047", 
    #"751253bf92ae4d99420f9a83ca3133c1", 

    #"4f552627030d14b2167910dd23e630e0",
    #"d43138ac58faba6edb66fd4e1c960ae6",
    #"50ef88b85b47b44130c117deed6cbe03",

    #"4c500220f72a81fc6e3492a8c6f5f8ac",
    #"64bb2058eb8f0b5d1f6eb87aca378db2",
    #"d4d2498b24a5835f2fa4f36691c99856",

    #'2ae16bfc5b3cf03d13dbaf3ea300daa0',
    #'47eb4c531a0d1ffd507c61ec74b6003f',
    #'9d1c7c1a1cf1d7cb1823fc6618d20d25',
    
    #'09c4b456ab4690037e8593f18068595a', 
    #'2d99b860676ff6f2b69488ed4992a99f', 
    #'c9da820f072dada13782cb43587072e4', 

    '20e087d3dea4acba979d34a58096aae4', 
    '6fe29d8ff65694e54d2579db9bb5a60f', 
    'bc6a0a5dbdfae33d08067932701bd7ae', 
]

#hosts = []
#with open('hosts.txt', 'r') as reader:
#    # Read and print the entire file line by line
#    line = reader.readline()
    #print(line)
#    while line != '':  # The EOF char is an empty string
#        print(line, end='')
#        line = reader.readline()
#        hosts.append(line)


token = ''
#token='eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlF6RXhNVEE0TWpOQlF6RXdRek14TURVeFJETTFNMEZDTlRCR05FSkRORUZGTVRsRlFqVTBNUSJ9.eyJodHRwczovL2FwcC5lbGVjdHJpYy5haS9zY29wZXMiOlsiZ2xvYmFsLmN1c3RvbWVyczpyZWFkIiwiZ2xvYmFsLmN1c3RvbWVyczp3cml0ZSIsImdsb2JhbC51c2VyczpyZWFkIiwiZ2xvYmFsLnVzZXJzOndyaXRlIl0sImlzcyI6Imh0dHBzOi8vZWxlY3RyaWMtc3RhZ2luZy5hdXRoMC5jb20vIiwic3ViIjoiSmRVb2ZaUFNOcDQxOERxOE1lSElrZTVrWnBQYVpZNjBAY2xpZW50cyIsImF1ZCI6Imh0dHBzOi8vZWxlY3RyaWMtc3RhZ2luZy5hdXRoMC5jb20vYXBpL3YyLyIsImlhdCI6MTYzMTIwMTY2OCwiZXhwIjoxNjMxMjg4MDY4LCJhenAiOiJKZFVvZlpQU05wNDE4RHE4TWVISWtlNWtacFBhWlk2MCIsInNjb3BlIjoicmVhZDpjbGllbnRfZ3JhbnRzIGNyZWF0ZTpjbGllbnRfZ3JhbnRzIGRlbGV0ZTpjbGllbnRfZ3JhbnRzIHVwZGF0ZTpjbGllbnRfZ3JhbnRzIHJlYWQ6dXNlcnMgdXBkYXRlOnVzZXJzIGRlbGV0ZTp1c2VycyBjcmVhdGU6dXNlcnMgcmVhZDp1c2Vyc19hcHBfbWV0YWRhdGEgdXBkYXRlOnVzZXJzX2FwcF9tZXRhZGF0YSBkZWxldGU6dXNlcnNfYXBwX21ldGFkYXRhIGNyZWF0ZTp1c2Vyc19hcHBfbWV0YWRhdGEgcmVhZDp1c2VyX2N1c3RvbV9ibG9ja3MgY3JlYXRlOnVzZXJfY3VzdG9tX2Jsb2NrcyBkZWxldGU6dXNlcl9jdXN0b21fYmxvY2tzIGNyZWF0ZTp1c2VyX3RpY2tldHMgcmVhZDpjbGllbnRzIHVwZGF0ZTpjbGllbnRzIGRlbGV0ZTpjbGllbnRzIGNyZWF0ZTpjbGllbnRzIHJlYWQ6Y2xpZW50X2tleXMgdXBkYXRlOmNsaWVudF9rZXlzIGRlbGV0ZTpjbGllbnRfa2V5cyBjcmVhdGU6Y2xpZW50X2tleXMgcmVhZDpjb25uZWN0aW9ucyB1cGRhdGU6Y29ubmVjdGlvbnMgZGVsZXRlOmNvbm5lY3Rpb25zIGNyZWF0ZTpjb25uZWN0aW9ucyByZWFkOnJlc291cmNlX3NlcnZlcnMgdXBkYXRlOnJlc291cmNlX3NlcnZlcnMgZGVsZXRlOnJlc291cmNlX3NlcnZlcnMgY3JlYXRlOnJlc291cmNlX3NlcnZlcnMgcmVhZDpkZXZpY2VfY3JlZGVudGlhbHMgdXBkYXRlOmRldmljZV9jcmVkZW50aWFscyBkZWxldGU6ZGV2aWNlX2NyZWRlbnRpYWxzIGNyZWF0ZTpkZXZpY2VfY3JlZGVudGlhbHMgcmVhZDpydWxlcyB1cGRhdGU6cnVsZXMgZGVsZXRlOnJ1bGVzIGNyZWF0ZTpydWxlcyByZWFkOnJ1bGVzX2NvbmZpZ3MgdXBkYXRlOnJ1bGVzX2NvbmZpZ3MgZGVsZXRlOnJ1bGVzX2NvbmZpZ3MgcmVhZDpob29rcyB1cGRhdGU6aG9va3MgZGVsZXRlOmhvb2tzIGNyZWF0ZTpob29rcyByZWFkOmVtYWlsX3Byb3ZpZGVyIHVwZGF0ZTplbWFpbF9wcm92aWRlciBkZWxldGU6ZW1haWxfcHJvdmlkZXIgY3JlYXRlOmVtYWlsX3Byb3ZpZGVyIGJsYWNrbGlzdDp0b2tlbnMgcmVhZDpzdGF0cyByZWFkOnRlbmFudF9zZXR0aW5ncyB1cGRhdGU6dGVuYW50X3NldHRpbmdzIHJlYWQ6bG9ncyByZWFkOnNoaWVsZHMgY3JlYXRlOnNoaWVsZHMgdXBkYXRlOnNoaWVsZHMgZGVsZXRlOnNoaWVsZHMgcmVhZDphbm9tYWx5X2Jsb2NrcyBkZWxldGU6YW5vbWFseV9ibG9ja3MgdXBkYXRlOnRyaWdnZXJzIHJlYWQ6dHJpZ2dlcnMgcmVhZDpncmFudHMgZGVsZXRlOmdyYW50cyByZWFkOmd1YXJkaWFuX2ZhY3RvcnMgdXBkYXRlOmd1YXJkaWFuX2ZhY3RvcnMgcmVhZDpndWFyZGlhbl9lbnJvbGxtZW50cyBkZWxldGU6Z3VhcmRpYW5fZW5yb2xsbWVudHMgY3JlYXRlOmd1YXJkaWFuX2Vucm9sbG1lbnRfdGlja2V0cyByZWFkOnVzZXJfaWRwX3Rva2VucyBjcmVhdGU6cGFzc3dvcmRzX2NoZWNraW5nX2pvYiBkZWxldGU6cGFzc3dvcmRzX2NoZWNraW5nX2pvYiByZWFkOmN1c3RvbV9kb21haW5zIGRlbGV0ZTpjdXN0b21fZG9tYWlucyBjcmVhdGU6Y3VzdG9tX2RvbWFpbnMgdXBkYXRlOmN1c3RvbV9kb21haW5zIHJlYWQ6ZW1haWxfdGVtcGxhdGVzIGNyZWF0ZTplbWFpbF90ZW1wbGF0ZXMgdXBkYXRlOmVtYWlsX3RlbXBsYXRlcyByZWFkOm1mYV9wb2xpY2llcyB1cGRhdGU6bWZhX3BvbGljaWVzIHJlYWQ6cm9sZXMgY3JlYXRlOnJvbGVzIGRlbGV0ZTpyb2xlcyB1cGRhdGU6cm9sZXMgcmVhZDpwcm9tcHRzIHVwZGF0ZTpwcm9tcHRzIHJlYWQ6YnJhbmRpbmcgdXBkYXRlOmJyYW5kaW5nIHJlYWQ6bG9nX3N0cmVhbXMgY3JlYXRlOmxvZ19zdHJlYW1zIGRlbGV0ZTpsb2dfc3RyZWFtcyB1cGRhdGU6bG9nX3N0cmVhbXMgY3JlYXRlOnNpZ25pbmdfa2V5cyByZWFkOnNpZ25pbmdfa2V5cyB1cGRhdGU6c2lnbmluZ19rZXlzIiwiZ3R5IjoiY2xpZW50LWNyZWRlbnRpYWxzIn0.vnnhKzW81UNao5s9MB0rp7blfSQVDwFdxfC6vQVpu2ybTj0aeQp7xd_z2Pm_lq44_61VMLP3LfCR6_xz-s-co0tAU4L_0TED4h9GonRRu-ndh1tbVOw2-FuEKI1oWLx8Y8IzrZ3fQlhl2rb8ARsSjWQSvYHfIWjaxTxc2e4L7OHntJAsWNa5lB6Dr4N2f1sPfaPYgWyAjMTcmnbMUA6D53HDHLuY-L76fAlzSRZ6_YNKjgVb0nQ8RAnqrS8vQh66ma1949nvnReZLLRO-PpzODqgbZ5kNGyQEtva5EgV0i_Z0aLPPfFozeMqAbS6tcbLgZcJVgZEErfGSHvcd65XLg'

#headers = {"Authorization": "Bearer " + token}
headers = {'Content-Type': "application/json", 'Accept': "application/json", "Authorization": "Bearer " + token}

#data = {}
#data = {"assigned_to": "4b74a197-09f6-4347-8ed7-5f8ff5165139", "assigned_by": "9a919a42-b506-49ee-b053-402827b761b7"}


data={}
data['assigned_by']="9a919a42-b506-49ee-b053-402827b761b7"
#data['assigned_to']="4b74a197-09f6-4347-8ed7-5f8ff5165139"
print(data)


users = [
    "4b74a197-09f6-4347-8ed7-5f8ff5165139", 
    "1b940372-8044-4de8-a326-f62fe0952767",
    "1b940372-8044-4de8-a326-f62fe0952767",
]

customer = "9a919a42-b506-49ee-b053-402827b761b7"

idx = 0
for host in hosts: 
    
    data['assigned_to'] = users[idx]

    print('\n\n')

    #url = ep_0 + host + ep_1
    url = ep_0 + customer + "::" + host + ep_1

    print('Endpoint: ', url)
    print('Data: ', data)
    print('PUT\n')

    idx += 1

    try: 
        #r = requests.put(url, data=data, headers=headers)
        #r = requests.put(url, json=data, headers=headers, auth=('Username', 'Password'))
        r = requests.put(url, json=data, headers=headers)

        print(r)
        
        #print(r.content)
        #print()
        #print(r.headers['content-type'])
        #print()
        #print(r.encoding)
        #print()
        print(r.text)
        #print()

        print(r.status_code)
        print('Server OK\n')

    except: 
        print('Error !')
        print('Impossible to connect')

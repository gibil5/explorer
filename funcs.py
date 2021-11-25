
org_customer_fields = [
    'id',
    'name',
    'avatar',
    'plan',
    'account_type',
    'status',

    'sf_account_id',
    'point_of_contact_id',

    'created_at',
    'updated_at',
    'activated_at',
    'discarded_at',
]

org_employee_fields = [
    'id', 
    'customer_id', 
    'email', 
    'first_name', 
    'last_name', 
    'phone', 
    'roles', 

    'auth0_id', 
    'avatar', 

    'electric', 
    'vip', 
    'approver', 
    'primary_approver', 
    'gsuite_admin',

    'created_at', 
    'updated_at', 
    'discarded_at', 
    'subscribed_at', 

]

org_office_fields = [
    'id', 
    'customer_id', 

    'name', 
    'phone', 

    'address_1', 
    'address_2', 
    'city', 
    'state', 
    'country',

    'postcode', 

    'verified', 
    'display_on_policies',
    'contact_id', 

    'created_at', 
    'updated_at', 
    'discarded_at',
]

def decode_api_organizations(r, entity):
    print('Decode api-organizations')

    if entity == 'offices':
        data_json = []
        data_json.append(r.json()['result'])
    else:
        data_json = r.json()['result']

    #print(data_json)

    if entity == 'customers':
        fields = org_customer_fields

    if entity == 'employees':
        fields = org_employee_fields

    if entity == 'offices':
        fields = org_office_fields

    idx = 0
    for data in data_json:
        print(idx)
        #print(data)
        for field in fields:
            print(field + ':\t', data[field])
        print()
        idx += 1

    print(len(data_json))
    print()


def decode_api_devices(r):
    print('Decode api-devices')

    data_json = r.json()['data']
    print(data_json)
    idx = 0
    for d in data_json:
        if d['assigned']:
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

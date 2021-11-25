
def decode(r):
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

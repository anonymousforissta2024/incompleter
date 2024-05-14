#Source: https://stackoverflow.com/questions/66005371/problem-with-my-python-api-typeerror-object-of-type-set-is-not-json-serializa
try:
    infos = client.api(method='Infos.getInfos')
    clientj = client.api('Client.getList',params={
        'order':{},
        'pagination':{},
        'search':{'periodecreated_start':{int(1577836800)}
        }
    })
except sellsy_api.SellsyAuthenticateError as e: 
    print('Authentication failed ! Details : {}'.format(e))
except sellsy_api.SellsyError as e: 
    print(e) 
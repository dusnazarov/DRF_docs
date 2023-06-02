
# #  ////////////////    Token Authorization    ///////////////////////
import requests

headers = {'Authorization':'Bearer 16fe711f45698c3c445429bf87babc9ae81a1f7e'}
endpoint = "http://127.0.0.1:8000/api/create/"

data = {
    "username":"ahror",
    "first_name":'Ahror',
    "last_name":"Mo'minjonov"
       
}

get_response = requests.post(endpoint, json=data, headers=headers)
print(get_response.json())
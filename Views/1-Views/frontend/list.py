# 1) //////////////////////  Class-based Views   ////////////////////////////
# import requests
# from getpass import getpass

# auth_endpoint = "http://127.0.0.1:8000/api/auth/"

# username = input("What is your username?\n")
# password = getpass("What is your password?\n")

# auth_response = requests.post(auth_endpoint, json={"username":username, "password":password })
# print(auth_response.json())

# if auth_response.status_code == 200:
#     token = auth_response.json()['token']
  
#     headers = {
#         "Authorization": f"Bearer {token}"
#     }
#     endpoint = "http://127.0.0.1:8000/api/list/"
#     get_response = requests.get(endpoint, headers=headers)
    
#     print(get_response.json())


# # 2) //////////////////////  Function-based Views   ////////////////////////////
# import requests

# endpoint = "http://127.0.0.1:8000/api/"
# get_response = requests.get(endpoint)

# print(get_response.json())

# 3) //////////////////////  Function-based Views   ////////////////////////////
import requests

endpoint = "http://127.0.0.1:8000/api/"
data = {
    'title':'good book',
    'content':'This book is my book'
}
get_response = requests.get(endpoint)
# get_response = requests.post(endpoint, json=data)

print(get_response.json())


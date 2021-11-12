import requests

base_url= "http://127.0.0.1:8000/"
endpoint_url = 'emp_api/'
final_url = base_url+endpoint_url
response = requests.get(final_url)
dict_data = response.json()
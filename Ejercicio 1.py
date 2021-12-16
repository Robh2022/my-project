import requests

param1 = "1"
param2 = "2"
url = "https://ammtp.pythonanywhere.com/testapp/get_example"
parametros = {
    "param1": param1,
    "param2": param2,
}
response = requests.get(url, params=parametros)
print(response.text)
valor1 = response.json()['request']['params']['param1']
valor2 = response.json()['request']['params']['param2']
assert valor1 == param1
assert valor2 == param2

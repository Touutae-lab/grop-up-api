import requests
URL="http://127.0.0.1:5000/get"
respoonds = requests.get(URL)
print(respoonds.json())
import requests

respons = requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

details = respons.json()

print(details[2] ["user"] ["url"])
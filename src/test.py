import requests

res = requests.get("http://hipsum.co/api/?type=hipster-centric&sentences=3")
print(res.content.decode())
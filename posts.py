import requests

r = requests.get(
    "http://127.0.0.1:8000/api/posts/?format=json",
    headers={"Authorization":"Token a9511383a5ad44f0448d06518b4bed0be3f1144b"}
)

print(r.json())
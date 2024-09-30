import requests


response = requests.post(
    "http://127.0.0.1:8080/advertisement",
    json={
        'title': 'New',
        'description': 'TV',
        'price': 125.50,
        'author': 'Yura'
    }
)

# response = requests.get("http://127.0.0.1:8080/advertisement/1")

# response = requests.patch("http://127.0.0.1:8080/advertisement/1",
#                           json={
#                               'description': 'Iphone New Model',
#                               'price': 130.0,
#                                 }
#                           )

# response = requests.delete("http://127.0.0.1:8080/advertisement/1")

# response = requests.get("http://127.0.0.1:8080/advertisement?qs_params=TV")

print(response.status_code)
print(response.json())

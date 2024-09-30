import requests


response = requests.post(
    "http://127.0.0.1:8080/advertisement",
    json={
        'title': 'Telephone',
        'description': 'Samsung',
        'price': 128.75,
        'author': 'Ivan'
    }
)

# response = requests.get("http://127.0.0.1:8080/advertisement/3")

# response = requests.patch("http://127.0.0.1:8080/advertisement/3",
#                           json={
#                               'description': 'Iphone New Model',
#                               'price': 135.0,
#                                 }
#                           )

# response = requests.delete("http://127.0.0.1:8080/advertisement/1")

# response = requests.get("http://127.0.0.1:8080/advertisement?qs_params=Sam")

print(response.status_code)
print(response.json())

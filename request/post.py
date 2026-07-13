import requests

data={
"name":"John"
}

response=requests.post(
"https://jsonplaceholder.typicode.com/posts",
json=data
)

print(response.json())
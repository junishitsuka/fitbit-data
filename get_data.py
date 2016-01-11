# coding: utf-8

import requests, json, os

TOKEN = os.getenv("GITHUB_API_TOKEN")

headers = {
    "Authorization": TOKEN
}

contents = {
    "message": "test commit",
    "commiter": {
        "name": "junishitsuka",
        "email": "ishitsuka.jun@gmail.com"
    },
    "content": "sample"
}

result = requests.put(
    "https://api.github.com/repos/junishitsuka/fitbit-data/contents/test.csv",
    headers = headers,
    data = json.dumps(contents)
)
print result

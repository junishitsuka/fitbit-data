# coding: utf-8

import requests, json, os, base64, fitbit
from datetime import datetime, timedelta

FITBIT_CONSUMER_KEY = ""
FITBIT_CONSUMER_SECRET = ""
FITBIT_USER_KEY = ""
FITBIT_USER_SECRET = ""
FITBIT_USER_ID = ""
GITHUB_API_TOKEN = ""

def fetch_fitbit_sleep_data(string_date):
    client = fitbit.Fitbit(
        FITBIT_CONSUMER_KEY,
        FITBIT_CONSUMER_SECRET,
        resource_owner_key = FITBIT_USER_KEY,
        resource_owner_secret = FITBIT_USER_SECRET,
        user_id = FITBIT_USER_ID,
        system = "ja-JP"
    )
    return client.sleep(string_date)

def push_github(data, string_date):
    headers = {
        "Authorization": "token " + GITHUB_API_TOKEN
    }

    contents = {
        "message": "sleep data of %s" % string_date,
        "commiter": {
            "name": "junishitsuka",
            "email": "ishitsuka.jun@gmail.com"
        },
        "content": base64.b64encode(data)
    }

    result = requests.put(
        "https://api.github.com/repos/junishitsuka/fitbit-data/contents/sleep/%s.json" % string_date,
        headers = headers,
        data = json.dumps(contents)
    )
    return result.content

# this function must be executed after sleep
# def lambda_handler(event, context):
if __name__ == "__main__":
    string_date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    data = fetch_fitbit_sleep_data(string_date)
    push_github(str(data), string_date)

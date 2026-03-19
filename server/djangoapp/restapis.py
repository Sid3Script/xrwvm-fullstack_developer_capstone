import requests


# We are hardcoding these to ensure the .env file doesn't override them
backend_url = "http://127.0.0.1:3031"
sentiment_url = "http://127.0.0.1:5000"


def get_request(endpoint, **kwargs):
    params = ""
    if (kwargs):
        for key, value in kwargs.items():
            params = params + key + "=" + str(value) + "&"

    # Fix potential slash issues
    if not endpoint.startswith('/'):
        endpoint = '/' + endpoint

    request_url = backend_url + endpoint + "?" + params

    print(f"DEBUG: Attempting to GET from {request_url}")

    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            return response.json()
        else:
            print(f"DEBUG: Server returned status {response.status_code}")
            return None
    except Exception as err:
        print(f"DEBUG: Network error: {err}")
        return None


def analyze_review_sentiments(text):
    request_url = f"{sentiment_url}/analyze/{text}"
    try:
        response = requests.get(request_url)
        if response.status_code == 200:
            return response.json()
        else:
            return {"sentiment": "neutral"}
    except Exception as err:
        print(f"DEBUG: Sentiment error: {err}")
        return {"sentiment": "neutral"}


def post_review(data_dict):
    request_url = backend_url + "/insert_review"
    try:
        response = requests.post(request_url, json=data_dict)
        return response.json()
    except Exception as err:
        print(f"DEBUG: Post error: {err}")
        return None

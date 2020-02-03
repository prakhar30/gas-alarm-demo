import requests


def post_request_with_url(params, headers):
    try:
        response = requests.post("https://us-central1-teravalve-90327.cloudfunctions.net/updateStatus", json=params, headers=headers)
        json_response = response.json()
        return json_response
    except requests.exceptions.RequestException as e:
        print(e)
        return None

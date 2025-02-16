import requests


def validate_api_endpoint(url):
    response = requests.get(url)

    # Validate status code
    if response.status_code != 200:
        print(f"Failed: Status code is {response.status_code}")
        return False

    # Validate response body
    try:
        data = response.json()
    except ValueError:
        print("Failed: Response is not in JSON format")
        return False

    print("Success: API endpoint is valid")
    return True

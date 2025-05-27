import requests
import os

API_URL = "https://app.nocodb.com/api/v2/tables/msj6ml4z41b2mp1/records"
API_TOKEN = os.getenv("NOCODB_API_TOKEN")
if not API_TOKEN:
    print("Error: NOCODB_API_TOKEN environment variable is not set.")
    exit(1)

params = {"offset": 0, "limit": 25, "where": "", "viewId": "vwb4pjfq0xu4291e"}

headers = {"xc-token": API_TOKEN}


def list_records():
    try:
        response = requests.get(API_URL, headers=headers, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        print("Records:")
        for record in data.get("list", []):
            print(record)
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP error occurred: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print("Error connecting to the API. Please check your network.")
    except requests.exceptions.Timeout as errt:
        print("Request timed out.")
    except requests.exceptions.RequestException as err:
        print(f"An error occurred: {err}")


if __name__ == "__main__":
    list_records()

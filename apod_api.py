import requests

def get_apod_data(api_key: str = "DEMO_KEY"):
    # https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=2
    url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}&count=2"
    response = requests.get(url, headers={"Accept": "application/json"}, timeout=10, verify=False)
 
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to retrieve data"}


def main():
    api_key = "DEMO_KEY"  # Replace with your actual API key from NASA
    apod_data = get_apod_data(api_key)
    print("APOD Data:")
    print(apod_data)   

if __name__ == "__main__":
    main()
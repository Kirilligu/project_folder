import requests

base_url = "http://localhost:8000"

def register_collar(unique_number, characteristics):
    response = requests.post(
        f"{base_url}/devices/collars",
        json={"unique_number": unique_number, "characteristics": characteristics}
    )
    return response.json()

if __name__ == "__main__":
    unique_number = "collar123"
    characteristics = "Color: Red, Size: M"
    result = register_collar(unique_number, characteristics)
    print(result)

import requests

def register_collar(collar_number: str):
    url = "http://localhost:8000/collars/"
    data = {"collar_number": collar_number}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Collar registered successfully")
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    collar_number = input("Enter collar number: ")
    register_collar(collar_number)


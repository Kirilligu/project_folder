import requests

def create_task(dog_id: int, api_key: str):
    url = f"http://localhost:8000/tasks/?api_key={api_key}"
    data = {"dog_id": dog_id}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Task created successfully")
    else:
        print("Error:", response.text)

def update_task_status(task_id: int, status: str, api_key: str):
    url = f"http://localhost:8000/tasks/{task_id}/update-status/?api_key={api_key}"
    data = {"status": status}
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Task status updated successfully")
    else:
        print("Error:", response.text)

if __name__ == "__main__":
    api_key = input("Enter API key: ")
    dog_id = int(input("Enter dog ID: "))
    create_task(dog_id, api_key)
    
    task_id = int(input("Enter task ID to update status: "))
    status = input("Enter new status: ")
    update_task_status(task_id, status, api_key)


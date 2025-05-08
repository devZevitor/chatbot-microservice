import httpx
import json

URL = "http://localhost:3333"
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJhMDU0NmRhNi05ZjgwLTQ1NjYtYjg3Yi0xZDI5YWZlZWNiMjAiLCJpYXQiOjE3NDYzMTU5MTEsImV4cCI6MTc0NjMyMzExMX0._Yty1XnNVAGIzqApywCk-t_Dn0yCIlgo1WZcruYrc_s"
def getSchedules():
    response = httpx.get(f"{URL}/schedules/free", headers={"Authorization": f"Bearer {token}"})

    if (response.status_code == 200):
        data = response.json()
        print(json.dumps(data, indent=2))
        return data
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None
    

def getSheculesByDay(day):
    response = httpx.get(f"{URL}/schedules/free/day/{day}", headers={"Authorization": f"Bearer {token}"})

    if (response.status_code == 200):
        data = response.json()
        print(json.dumps(data, indent=2))
        return data
    else: 
        print(f"Error: {response.status_code} - {response.text}")
        return None
    
def getHairDresser():
    response = httpx.get(f"{URL}/schedules/hairDresser", headers={"Authorization": f"Bearer {token}"})

    if(response.status_code == 200):
        data = response.json()
        print(json.dumps(data, indent=2))
        return data
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None
    
def getTypeServices():
    response = httpx.get(f"{URL}/schedules/type", headers={"Authorization": f"Bearer {token}"})

    if(response.status_code == 200):
        data = response.json()
        print(json.dumps(data, indent=2))
        return data
    else:
        print(f"Erro: {response.status_code} - {response.text}")
        return None
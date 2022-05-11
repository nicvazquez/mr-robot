import requests
from utilities.variables import udemyApiAuthorization

def getCourses():
    url = "https://www.udemy.com/api-2.0/courses/?page=1&page_size=100&price=price-free"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": udemyApiAuthorization,
        "Content-Type": "application/json;charset=utf-8"
    }
    response = requests.get(url, headers=headers).json()

    return response
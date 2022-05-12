import requests
from utilities.variables import udemyApiAuthorization
from random import randint

def getCourses():
    page = randint(1, 10000) # get a random course
    url = f"https://www.udemy.com/api-2.0/courses/?page={page}&page_size=1&price=price-free"
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Authorization": udemyApiAuthorization,
        "Content-Type": "application/json;charset=utf-8"
    }
    response = requests.get(url, headers=headers).json()

    return response

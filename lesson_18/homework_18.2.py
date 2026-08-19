import requests


BASE_URL = "http://127.0.0.1:8080"
IMAGE_NAME = "mars_photo1.jpg"


# POST - завантажуємо фото
with open(IMAGE_NAME, "rb") as image:
    files = {
        "image": (IMAGE_NAME, image, "image/jpeg")
    }

    response = requests.post(
        f"{BASE_URL}/upload",
        files=files
    )

print("POST:", response.status_code)
print(response.json())


# GET - отримуємо URL фото
headers = {
    "Content-Type": "text"
}

response = requests.get(
    f"{BASE_URL}/image/{IMAGE_NAME}",
    headers=headers
)

print("\nGET:", response.status_code)
print(response.json())


# DELETE - видаляємо фото
response = requests.delete(
    f"{BASE_URL}/delete/{IMAGE_NAME}"
)

print("\nDELETE:", response.status_code)
print(response.json())
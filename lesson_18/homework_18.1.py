import requests


NASA_API = "https://images-api.nasa.gov"

params = {
    "q": "Mars Curiosity",
    "media_type": "image",
    "page_size": 15
}

search = requests.get(f"{NASA_API}/search", params=params)

if search.status_code != 200:
    print("Не вдалося виконати пошук")
else:
    results = search.json()["collection"]["items"]

    photo_number = 1

    for result in results:
        nasa_id = result["data"][0]["nasa_id"]

        assets = requests.get(f"{NASA_API}/asset/{nasa_id}")
        asset_list = assets.json()["collection"]["items"]

        jpg_link = None

        for asset in asset_list:
            link = asset["href"]

            if link.lower().endswith(".jpg"):
                jpg_link = link
                break

        if jpg_link:
            picture = requests.get(jpg_link)

            file_name = f"mars_photo{photo_number}.jpg"

            with open(file_name, "wb") as image_file:
                image_file.write(picture.content)

            print(f"Збережено {file_name}")

            photo_number += 1

        if photo_number > 2:
            break
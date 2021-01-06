from pathlib import Path
import requests
import shutil
import time

url = 'https://thispersondoesnotexist.com/image'


def get_image(index):
    response = requests.get(url, stream=True)
    with open('image/img' + str(index) + '.jpg', 'wb') as file:
        shutil.copyfileobj(response.raw, file)


if __name__ == "__main__":
    print("This python script will download images from thispersondoesnotexist.com")
    print("Please, put indexes for images [a, b]")
    print("They will save as images/img*.jpg where * = [a, b]")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    Path('image').mkdir(parents=True, exist_ok=True)
    for i in range(a, b + 1):
        print(f"Downloading img{i}.jpg...")
        get_image(i)
        time.sleep(1)

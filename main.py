import requests
import shutil
import time

url = 'https://thispersondoesnotexist.com/image'


def get_image(index):
    response = requests.get(url, stream=True)
    with open('img' + str(index) + '.jpg', 'wb') as file:
        shutil.copyfileobj(response.raw, file)


for i in range(1, 101):
    print(i)
    get_image(i)
    time.sleep(1)

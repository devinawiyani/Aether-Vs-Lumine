from selenium import webdriver
import requests
import io
from PIL import Image

PATH = r'D:\Chrome web driver\chromedriver-win64\chromedriver.exe'

wd=webdriver.Chrome(PATH)

def download_image (download_path, url, file_name):
    image_content= requests.get(url).content
    image_file=io.BytesIO(image_content)
    image = image.open(image_file)
    file_path=download_path + file_name

    with open(file_path,"wb") as f:
        image.save(f, "PNG")
    
    print("Success")
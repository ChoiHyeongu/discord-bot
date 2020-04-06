#-*- coding:utf-8 -*-
from google_images_download import google_images_download
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

def get_orogzi_image():
    keyword = "오로지 널 이기고싶어 오로지 사진"
    response = google_images_download.googleimagesdownload()

    arguments = {
        "keywords":"dog",
        "limit": 100,
        "print_urls": True,
        "no_directory": True,
    }

    path = response.download(arguments)
    print(path)

get_orogzi_image()
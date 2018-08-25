# -*- coding: utf-8 -*-
import urllib.error
import urllib.request

def download_imgs(url, path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

url = input('url: ')
path = input('保存先: ')

download_imgs(url, path)

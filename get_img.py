# -*- coding: utf-8 -*-
import urllib.error
import urllib.request
import os

def make_filename(base_dir, number, url):
    ext = os.path.splitext(url)[1] # 拡張子を取得
    filename = number + ext        # 番号に拡張子をつけてファイル名にする

    fullpath = os.path.join(base_dir, filename)
    return fullpath

def download_img(url, path):
    try:
        data = urllib.request.urlopen(url).read()
        with open(path, mode="wb") as f:
            f.write(data)
    except urllib.error.URLError as e:
        print(e)

path = input('保存フォルダ:')

url = input('url: ')                    #画像のurl。.pngとかになることを想定。
fullpath = make_filename(path,'0',url)  #ここの第２変数を回す変数にする。文字列型。
download_img(url, fullpath)

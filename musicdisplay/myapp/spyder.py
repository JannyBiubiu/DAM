# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import sys
import urllib
import json
import re
import requests
from PIL import Image
from config import FOLDER,CATEGORY,LISTID 

#配置webdriver
chrome_options=Options()
chrome_options.add_argument('-headless')
chromedriver="./chromedriver.exe"
driver = webdriver.Chrome(chromedriver,chrome_options=chrome_options)

#获取隐藏html文件
def getHttp(url):
	driver.get(url)
	iframe = driver.find_elements_by_tag_name('iframe')[0]
	driver.switch_to.frame(iframe)	  # 最重要的一步
	soup = BeautifulSoup(driver.page_source, "html.parser")
	return soup

##############
#基于网易云音乐搜索页面的歌单一栏url，获取歌单id
#基于歌单id，获取歌曲id
#基于歌曲id，获取歌曲mp3，基本信息（曲名、作者、专辑），歌词，封面图，并且将歌曲id录入meta中，包括是否有歌词
##############

#获取指定页面的歌单id
def getlist(url):
	soup = getHttp(url)
	data= soup.select('td > div > div > div > span > a')
	return data

#已知歌单id，获取歌曲id
def getsongid(href):
	url="https://music.163.com/#"+href
	soup=getHttp(url)
	data=soup.select('td > div > div > div > span > a')
	return data

#已知歌曲id，获取基本信息和封面图片并卸载到指定路径
def getimg_descript(object):
	songid=object["id"]
	url='https://music.163.com/#/song?id='+songid
	filepath=FOLDER+"/"+songid+'.png'
	soup=getHttp(url)
	keywords=soup.select('meta')[5]
	keywords=keywords.get('content')
	keywords=keywords.split("，")
	object["title"]=keywords[0]
	descript=soup.select('meta')[6]
	descript=descript.get('content')
	descript=descript.split("。")
	object["artist"]=descript[0][3:]
	object["album"]=descript[1][5:]
	img_url=soup.select('meta')[9]
	img_url=img_url.get('content')
	im=Image.open(urllib.request.urlopen(img_url))
	im.save(filepath,"png")
	object["img"]="."+filepath

#已知歌曲id，获取MP3并加载到指定路径
def getsong(object):
	songid=object["id"]
	url='http://music.163.com/song/media/outer/url?id='+songid+'.mp3'
	filepath=FOLDER+"/"+songid+'.mp3'
	f=urllib.request.urlopen(url)
	with open(filepath,"wb") as code:
		code.write(f.read())
	object["media"]="."+filepath

#已知歌曲id，获取歌曲歌词
def getlyrics(object):
	songid=object["id"]
	url='http://music.163.com/api/song/lyric?' + 'id=' + songid + '&lv=1&kv=1&tv=-1'
	filepath=FOLDER+'/'+songid+'.lrc'
	lyric=requests.get(url)
	json_obj=lyric.text
	j=json.loads(json_obj)
	if 'lrc' in j:
		lrc=j['lrc']['lyric']
		head="[ti:"+object["title"]
		with open(filepath,"wb") as code:
			code.write(bytes(lrc, encoding = "utf8") )
		object["lrc"]="."+filepath
	

if __name__ == '__main__':
	songs=getsongid('/playlist?id='+LISTID)
	for song in songs:
		id=song.get("href")[9:]
		song_object={}
		song_object["id"]=id
		song_object["category"]=CATEGORY
		getsong(song_object)
		getimg_descript(song_object)
		getlyrics(song_object)
		with open(FOLDER+"/meta.json","a+") as code:
			code.write(json.dumps(song_object))
			code.write("\n")


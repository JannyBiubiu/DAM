"""
Routes and views for the flask application.
"""
#-*- coding:utf-8 -*-
from datetime import datetime
from flask import render_template,request
from myapp import app
import os
import json

with open("./myapp/static/meta.json","r+",encoding="utf-8") as code:
	obj=json.load(code)
	fields=obj["media_src"]
def getmeta(path):
	list=[]
	with open(path,"r+",encoding="utf-8") as code:
		for line in code:
			obj=json.loads(line)
			list.append(obj)
	return list

@app.route('/')
@app.route('/home')
def home():
	return render_template(
	'index.html',
	title='主页',
	fields=fields,
	year =datetime.now().year,
	)
@app.route("/about")
def about():
	return render_template(
		'about.html',
		title='关于我',
		year=datetime.now().year,
		fields=fields
	)
@app.route("/#/<name>",methods=['post','get'])
def field(name):
	list=getmeta("./myapp/static/"+name+"/meta.json")
	return render_template(
		'field.html',
		title='分区',
		fields=fields,
		name=name,
		year =datetime.now().year,
		list=list
	)
@app.route("/#/<name>/<id>",methods=['post','get'])
def play(name,id):
	list=getmeta("./myapp/static/"+name+"/meta.json")
	data={}
	for song in list:
		if song["id"]==id:
			data=song
			break
	json_obj={}
	if 'lrc' in data:
		lrc="./myapp"+data["lrc"][2:]
		f=open(lrc,"r+",encoding="utf-8")
		lrcs=f.read()
		lrcs=lrcs.split('\n')
		for lrc in lrcs:
			list=lrc.split(']')
			if len(list)==1:
				continue
			if list[1]=="":
				continue
			value=list[-1]
			for j in range(len(list)-1):
				key_music=list[j][1:]
				key_time=key_music.split(':')
				music_time=float(key_time[0])*60+float(key_time[1])
				key=music_time
				json_obj[key]=value
	key_list=[]
	for key1 in json_obj.keys():
		key_list.append(key1)
	key_list.sort()
	return render_template(
		'play.html',
		fields=fields,
		title='播放',
		id=id,
		name=name,
		data=data,
		lyrics=json_obj,
		lyrics_key=key_list,
		year=datetime.now().year
		)
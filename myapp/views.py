#-*- coding:utf-8 -*-
from datetime import datetime
from flask import render_template,request,jsonify
from myapp import app
import base64
import cv2
import werkzeug
import os
import json
import numpy as np
from PIL import Image
import io
def bs64_cv(str):
	offset=str.find('base64,')
	str = base64.b64decode(str[(offset+7):])
	nparr = np.fromstring(str, np.uint8)
	return cv2.imdecode(nparr, cv2.IMREAD_COLOR)

@app.route('/')
@app.route('/generate')
def generate():
	return render_template(
	'index.html',
	title='生成',
	year =datetime.now().year,
	)
@app.route('/extract')
def extract():
	return render_template(
	'test.html',
	title='提取',
	year =datetime.now().year,
	)
@app.route('/upload_mark',methods=['POST'])
def upload_mark():
	data=request.get_json()
	data=data['data']
	img=data['base64']
	img_np = bs64_cv(img)
	img_np=img_np//64*64
	cv2.imwrite("mark.png", img_np, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) 
	image = cv2.imencode('.png', img_np)[1]
	base64_data = str(base64.b64encode(image))[2:-1]
	base64_data='data:image/png;base64,'+base64_data
	return jsonify(data=base64_data)
@app.route('/upload_img',methods=['POST'])
def upload_img():
	data=request.get_json()
	data=data['data']
	img=data['base64']
	img_np =bs64_cv(img)
	img_np=img_np//4*4
	cv2.imwrite("img.png", img_np, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) 
	image = cv2.imencode('.png', img_np)[1]
	base64_data = str(base64.b64encode(image))[2:-1]
	base64_data='data:image/png;base64,'+base64_data
	return jsonify(data=base64_data)
@app.route('/generate_img',methods=['POST'])
def generate_img():
	img=cv2.imread("img.png")  
	mark=cv2.imread("mark.png")
	mark = cv2.resize(mark, (img.shape[1], img.shape[0]), interpolation=cv2.INTER_CUBIC)
	new_img=mark//64+img
	image = cv2.imencode('.png', new_img)[1]
	base64_data = str(base64.b64encode(image))[2:-1]
	base64_data='data:image/png;base64,'+base64_data
	return jsonify(data=base64_data)

@app.route('/extract_img',methods=['POST'])
def extract_img():
	data=request.get_json()
	data=data['data']
	img=data['base64']
	img_np = bs64_cv(img)
	img_np=img_np%4*64
	cv2.imwrite("img.png", img_np, [int(cv2.IMWRITE_PNG_COMPRESSION), 0]) 
	image = cv2.imencode('.png', img_np)[1]
	base64_data = str(base64.b64encode(image))[2:-1]
	base64_data='data:image/png;base64,'+base64_data
	return jsonify(data=base64_data)
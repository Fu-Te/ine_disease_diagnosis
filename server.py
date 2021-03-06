from flask import Flask, render_template,request
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.models import load_model
import numpy as np
from image_process import examine_ine
from datetime import datetime
import os 
import cv2
import pandas as pd
from PIL import Image

app=Flask(__name__)


@app.route('/',methods=['GET', 'POST'])
def upload_file():
	if request.method=='GET':
		return render_template('index.html')

	if request.method=="POST":
		#uploadファイルの保存
		f=request.files['file']
		filepath='./static/'+datetime.now().strftime("%Y%m%d%H%M%S")+'.png'
		f.save(filepath)



		#健康を調べる関数の実行
		result = examine_ine(filepath)

		if result>75:
			rice_status='病気の可能性高'
		elif result>50:
			rice_status='病気の可能性有り'
		elif result>30:
			rice_status='病気の可能性低'
		else:
			rice_status='健康'

		print(result)
		print('result')



		return render_template('index.html',filepath=filepath,
		result=result,rice_status=rice_status)

if __name__=='__main__':
	app.debug=True
	app.run(host='localhost',port=5000)

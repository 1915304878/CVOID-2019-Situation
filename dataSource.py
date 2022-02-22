import re
import json
import pymysql
import requests
from urllib3 import *
from datetime import date
disable_warnings()

db = pymysql.connect(
	host = 'localhost',
	user = 'root', 
	password = 'james123',
	db = 'CVOID2019'
)

# mysql 初始化
cursor = db.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS detailCount (
	date date NOT NULL,
	provinceName varchar(20) NOT NULL,
	currentConfirmedCount int(10) NOT NULL,
	confirmedCount int(10) NOT NULL,
	deadCount int(10) NOT NULL,
	curedCount int(10) NOT NULL)""")

resp = requests.get('https://ncov.dxy.cn/ncovh5/view/pneumonia', verify=False)
data = re.findall(r'(?<=window.getAreaStat =).*?(?=}catch)', str(resp.content,'utf-8') )
data = json.loads(data[0])
for i in range(len(data)):
	cursor.execute('INSERT INTO detailCount (date, provinceName, currentConfirmedCount, confirmedCount, deadCount, curedCount) VALUES (%s, %s, %s, %s, %s, %s)', 
		(date.today(), data[i]['provinceName'], data[i]['currentConfirmedCount'], data[i]['confirmedCount'], data[i]['deadCount'], data[i]['curedCount'],))
db.commit()
db.close()

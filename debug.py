import json
import time
def setup():
	b=open('gameData/logs/latest_log.txt','w')
	b.truncate()	
def log(text):
	a=open('gameData/debugSettings.json','r')
	x=json.load(a)
	if(x['debug']==True):
		b=open('gameData/logs/latest_log.txt','w')
		print(time.ctime()+'  > '+str(text))
		b.write(time.ctime()+'  > '+str(text)+'\n')
		return(True)
	else:
		return(False)
import json
import time
def log(text):
	a=open('gameData/debugSettings.json','r')
	x=json.load(a)
	if(x['debug']==True):
		print(time.ctime()+'  > '+str(text))
		return(True)
	else:
		return(False)
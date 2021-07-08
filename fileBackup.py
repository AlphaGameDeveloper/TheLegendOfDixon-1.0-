import os
import json
def createFileSystem():
	os.mkdir('gameData')
	with open('gameData/debugSettings.json','w') as file:
		a={'debug':False}
		json.dump(a,file)
		file.close()
	os.mkdir('gameData/save/')
	with open('gameData/save/gameGame.json','w') as file:
		a={'isNewFile':True,'inventory':['default_sword'],'saveName':None,'heroName':None}
		json.dump(a,file)
		file.close()
	os.mkdir('gameData/logs')
	
	
	
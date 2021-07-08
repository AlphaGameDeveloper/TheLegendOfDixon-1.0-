import os
import json
def createFileSystem():
	os.mkdir('gameData')
	with open('gameData/debugSettings.json','w') as file:
		a={'debug':False}
		json.dump(a,file)
		file.close()
	
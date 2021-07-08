import json
from debug import log

def checkForFile(path):
	log('checkForFile() called.')
	try:
		with open(path,'r') as file:
			log('File at location < '+str(path)+' > exists.')
			return(True)
	except:
		log('File at location < '+str(path)+' > does not exist.')
def loadJsonFile(path):
	log('Loading '+path)
	with open(path,'r') as file:
		return(json.load(file))
import debug
import fileBackup
import gameLoader
try:
	fileBackup.createFileSystem()
	debug.setup()
	debug.log('Created file system.')
except:
	debug.log('Did not have to create file system, already created...')
	pass
debug.log('main.py: start')


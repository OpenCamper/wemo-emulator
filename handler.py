import os

'''
 This is a handler class to handle script execution on Alexa's request.
 The fauxmo class expects handlers to be instances of objects that have
 on() and off() methods that return True on success and False otherwise.
 
 This handler class takes the name of a script that should be located
 in ~/wemo-emulator/scripts and executes it on the on command.
 Alternatively also an off command script can be given.
'''

class script_handler(object):
	script_path = "~/wemo-emulator/scripts/{}"
	
	'''
	 init function for script handler object
	 
	 Arguments:
		on_script: string, name of the script executed with
			the 'on' command located in script_path
		off_script: string, name of the script executed with
			the 'off' command located in script_path
	'''
	def __init__(self, on_script, off_script = None):
		self.on_script = on_script
		self.off_script = off_script

	def on(self):
		success = os.system(script_handler.script_path.format(self.on_script))
		return not success

	def off(self):
		if not self.off_script:
			return False
		else:
			success = os.system(script_handler.script_path.format(self.off_script))
			return not success

if __name__ == '__main__':
	print(script_handler.script_path.format("test"))

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

class fct_handler (object):
	""" handle function callusing Alexa """
	
	def __init__ (self, on_fct, on_args, off_fct = None, off_args = None):
		""" initialize the functions that should be run on 'on' and 'off' cmds
		 on_fct/off_fct: function to be called on 'on/off' cmd
		 on_args: list of arguments for on/off_fct 
		"""
		self.on_fct = on_fct
		self.on_args = on_args
		self.off_fct = off_fct
		self.off_args = off_args
	
	def on (self):
		""" call on function """
		if type(self.on_args) == list:
			# unpack arguments and call function
			return self.on_fct(*self.on_args)
		
		# else call function with single argument
		return self.on_fct(self.on_args)
	
	def off (self):
		""" call off function """
		if self.off_fct != None:
			if type(self.off_args) == list:
				# unpack arguments and call functioff
				return self.off_fct(*self.off_args)
			
			# else call functioff with single argument
			return self.off_fct(self.off_args)
		
		return False

def square (x):
	""" -- test function --
	 square input
	"""
	try:
		print(x*x)
		return True
	except Exception as e:
		return False

def cube (x):
	""" -- test function --
	 cube input
	"""
	try:
		print(x*x*x)
		return True
	except Exception as e:
		return False

if __name__ == '__main__':
	print(script_handler.script_path.format("test"))
	
	# test fct_handler
	testhandler = fct_handler(square, 2, cube, 3)
	print("test on fct (square of 2) succeded? {}".format(testhandler.on()))
	print("test off fct (cube of 3) succeded? {}".format(testhandler.off()))

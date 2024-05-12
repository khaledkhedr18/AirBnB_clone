import cmd
class myCmd(cmd.Cmd):
	""" Simple command processing example """
	prompt = "khaled > "
	completekey = 'Tab'
	FRIENDS = [ 'khaled', 'Mazen', 'Os Os', 'Hazem' ]

	def do_greet(self, person):
		""" A function that greets the person
			hello [person]y
		"""
		if person and person in self.FRIENDS:
			greeting = "Hello, %s!" % person
		elif person:
			greeting = "Hello, " + person + "!"
		else:
			greeting = "Hello!"

		print(greeting)

	def complete_greet(self, text, line, begidx, endidx):
		if not text:
			completions = self.FRIENDS[:]
		else:
			completions = [f for f in self.FRIENDS if f.startswith(text)]
		return completions

	def do_exit(self, person):
		""" A function that exits the process
		bye [person]
		"""
		print("bye", person)
		return True
	def do_EOF(self, line):
		return True
	
if __name__ == '__main__':
	myCmd().cmdloop()
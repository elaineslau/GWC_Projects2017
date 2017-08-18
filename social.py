class User:
	def __init__(self, username, password):
		self.username = username
		self.password = password
		self.friends = []

def main():
	#instantiating
	User1 = User("Elaine","12345")


main()
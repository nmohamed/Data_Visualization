
class CommonPass():
	""" Common passwords """
	def __init__(self, pass_word, user_name):
		self.password = pass_word
		self.username = [user_name]
		self.occurance = 1

	def add_username(self, user_name):
		self.username.append(user_name)
		self.occurance += 1



_123456 = CommonPass("123456", username)
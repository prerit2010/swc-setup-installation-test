class A:
	def __init__(self, message):
		self.message = message
		# self.a = (("message",['sdsd','sdsdd']), (2,3))

	# def __repr__(self):
	# 	return self.message
	def __iter__(self):
		a = ((3,9), (5,6))
		return iter(a)
	def __getitem__(self):
		a = {"dfdf":"dfdfdf"}
		return a

print dict(A("Hello"))

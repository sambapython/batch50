def fun():
	print "this is fun in f2"
if True:
	def fun3():
		print "this is fun3 in f2"
def main():
	print "this is f2"
	def fun2():
		print "this is fun2 in f2"
	fun3()
	fun2()

if __name__ == "__main__":
	main()
	
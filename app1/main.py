import db_structure
while True:
	opt = raw_input("""
	DB Operations:
		1. insert
		2. update
		3. delete
		4. browse
		q. quit
	""")
	opt=opt.lower()
	if opt in ["q","quit"]:
		print "thank you!!"
		break
	elif opt=="1":
		db_structure.insert_customer()
	else:
		print "wrong option"
		

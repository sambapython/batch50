import unittest
from app import fun
class FunTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		print "login"
		cls.user="USER1"
	@classmethod
	def tearDownClass(cls):
		print "log out"
		cls.user=None
	def setUp(self):
		print "setting resource"
	def tearDown(self):
		print "deleting resource"
	def test_10_20(self):
		print "executing test_10_20 "
		print self.user
		exp_res=30
		act_res=fun(10,20)
		self.assertEqual(exp_res,act_res,"test_10_20 failed.")

	def test_str1_str2(self):
		print "executing test_str1_str2 "
		print self.user
		exp_res="str1str2"
		act_res=fun("str1","str2")
		self.assertTrue(exp_res==act_res,"test_str1_str2 failed.")
	def test_str1_10(self):
		print "executing test_str1_10 "
		print self.user
		exp_res=None
		act_res=fun("str1",10)
		self.assertEqual(exp_res,act_res,"test_str1_10 failed.")
	def test_20_str2(self):
		print "executing test_20_str2 "
		print self.user
		exp_res=None
		act_res=fun(20,"str2")
		self.assertEqual(exp_res,act_res,"test_20_str2 failed.")
	def fun1(self):
		print "this is normal method"
unittest.main()
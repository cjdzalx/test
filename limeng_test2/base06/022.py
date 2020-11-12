# -*- coding: utf-8 -*-
import unittest
class Test(unittest.TestCase):

	m = 1

	@classmethod
	def setUpClass(cls):  # 只执行了一次
		print("这也是前置条件")

	def setUp(self):
		print("这是前置条件")

	def test_a(self):
		print("这是第一条测试用例")
		self.assertEqual("a","b",msg="两个变量不等")   # 两个相等
		self.assertFalse("False")

	def test_b(self):
		print("这是第二条测试用例")

	# @unittest.skip
	# @unittest.skip("跳过原因")   # 无条件执行跳过测试用例执行
	# @unittest.skipIf(m==0,"m等于1的时候跳过")   # 执行条件满足，执行测试用例
	@unittest.skipUnless(m==1,"m等于1的时候跳过")
	def test_c(self):
		print("这是第三条测试用例")

	def tearDown(self):
		print("这是后置条件")

	@classmethod
	def tearDownClass(cls):   # 只执行的了一次
		print("这也是后置条件")

if __name__ == '__main__':
	unittest.main()  # 执行所有

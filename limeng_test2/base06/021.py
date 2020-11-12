# -*- coding: utf-8 -*-
# 异常处理
"""
NoSuchElementException：没有找到元素
NoSuchFrameException：没有找到iframe
NoSuchWindowException:没找到窗口句柄handle
NoSuchAttributeException:属性错误
NoAlertPresentException：没找到alert弹出框
lementNotVisibleException：元素不可见
ElementNotSelectableException：元素没有被选中
TimeoutException：查找元素超时
"""
class Error(Exception):
	def __init__(self,msg="大小错误"):   # 默认值不写也可以
		Exception.__init__(self,msg)

a = 100
if a<=100:
	# raise Error()
	raise Error(msg="数值太小了！")
# -*- coding: utf-8 -*-
# 兔子
# 幼仔对数=前月成兔的对数
# 成兔对数=前月成兔的对数+前月幼仔对数
# 总体对数=本月幼仔对数+本月成兔对数
def rabbit(month):
	rabbits = [1,1]
	for i in range(1,month-1):
		if month<3:
			break
		else:
			x = rabbits[i-1] + rabbits[i]
			rabbits.append(x)
	return rabbits

print(rabbit(8))
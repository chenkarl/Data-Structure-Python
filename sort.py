def Locate(arr:list,fn) :
	length = len(arr)
	loc = 0
	for i in range(length) :
		if fn(arr[loc],arr[i]) :
			loc = i
	return loc

def StraightInsertSort(arr:list,reserve = True) -> list:
	'''
	直接插入排序
	arr 待排序数组
	reserve 反向标记
	思想：选择未排序中最小的到前面
	'''
	length = len(arr)
	if reserve :
		fn = lambda a,b : a > b
	else :
		fn = lambda a,b : a < b
	for i in range(length) :
		pos = Locate(arr[i:],fn)
		arr[i],arr[i + pos] = arr[i + pos],arr[i]
	return arr

def QuickSort(arr:list, high:int, low:int, reserve = True) -> list:
	'''
	快速排序
	arr 待排序数组
	reserve 反向标记
	思想：左边都小于，右边都大于，递归
	'''
	left = high
	right = low
	pos = left
	dic = True
	while left < right :
		#print(arr)
		#print(dic)
		#print("left=",left,"pos=",pos,"right=",right)
		print("left=",arr[left],"pos=",arr[pos],"right=",arr[right])
		if dic :
			# 从右找比标记元素小的，直到找到
			while  arr[pos] <= arr[right] and pos < right :
				right -= 1
			arr[pos],arr[right] = arr[right],arr[pos]
			pos = right
		else :
			# 从左找比标记元素大的，直到找到
			while arr[pos] >= arr[left] and pos >left :
				left += 1
			arr[pos],arr[left] = arr[left],arr[pos]
			pos = left
		dic = not dic
	if high < pos - 1 :
		print("left")
		QuickSort(arr,high,pos - 1)
	if pos + 1 < low :
		print("right")
		QuickSort(arr,pos + 1,low)
	return arr

def BubberSort(arr:list, reserve:bool = True) :
	'''
	冒泡排序
	arr 待排序数组
	reserve 反向标记
	思想：两层循环
	时间复杂度：O(n2)
	'''
	length = len(arr)
	for i in range(0,length):
		for j in range(0,length-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]				

def main() :
	test = [23,31,49,31,6,19]
	print(test)
	# result = StraightInsertSort(test.copy())
	# QuickSort(test,0,len(test)-1)
	BubberSort(test)
	print(test)

if __name__ == "__main__" :
	main()
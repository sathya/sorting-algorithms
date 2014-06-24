import sys




def merge(left,right):
	try:
		i = j = 0
		result = []
		while i < len(left) and j < len(right) :
			if left[i] <= right[j]:
				result.append(left[i])
				i +=1
			else:
				result[j].append(right[j])
				j+=1
		result +=left[i:]
		result +=right[j:]
		return result
				
	except Exception as e:
		pass
	




def merge_sort(a):
	try:
		if a:
			if len(a) < 2:
				#one element in the a
				return a
			else:
				middle = int(len(a)/2)
				print ('middle is ',middle) 
				left   = merge_sort(a[:middle])
				right  = merge_sort(a[middle:])
				print (left,end = '\n')
				print (right,end ='\n')
				return merge(left,right)
	except Exception as e:
		print ('Exception Occured in the merge sort function\n' + str(e))
		

if __name__ =='__main__':
	a = [1,2,3,4,5,6,7,8,9]
	merge_sort(a)
	print (a)
import sys

def swap(a,i,j):
  #print ('coming to swap')
  a[i] = a[i] + a[j]
  a[j] = a[i] - a[j]
  a[i] = a[i] - a[j]
  


def bubble_sort(a, n):
	#print (id(a))
	done = False
	size = n
	while (done != True):
		done = True
		for i in range(size-1):
			if (a[i] > a[i+1]):
				swap(a,i,i+1)
				done = False
		size -=1		
	#	print('a inside',a)
	
if __name__ =='__main__':
	a = [10,9,8,7,6,1,2,3,4,5]
	#print (id(a))
	bubble_sort(a,len(a))
	#print (a)
	
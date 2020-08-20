while True:
	try:
		s = input()
	except EOFError:
		break
	
	first, second = s.split(',')
	first = first[::-1]
	second = second[::-1]
	
	res = int(first)+int(second)
	res = str(res)[::-1]
	
	print(int(res))

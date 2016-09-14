# def replicate_iter(times, data):
# 	try:
# 		if (times <= 0):
# 			return []
# 		return [data] * times

# 	except ValueError:
# 		return 'The provided input is invalid'

# def replicate_recur(times, data):
# 	try:
# 		if (times <= 0):
# 			return []
# 		return [data] + replicate_recur(times-1, data)
	
# 	except ValueError:
# 		return 'The provided input is invalid'

# def replicate_iter(times, data):
# 	if (times <= 0):
# 		return []
# 	else:
# 		return [data] * times
# 	raise ValueError("Invalid input")

# def replicate_recur(times, data):
# 	if (times<= 0):
# 		return []
# 	else:
# 		return [data] + replicate_recur(times-1, data)
# 	raise ValueError("Invalid input")

def replicate_iter(times, data):
	if (times <= 0):
		return []
	elif(times > 0):
		result = []
		for i in range (times+1):
			result.insert(i,data)
		return result
	else:
  		raise ValueError("Invalid input")
	
def replicate_recur(times, data):
	if (times <= 0):
		return []
	else:
		return [data] + replicate_recur(times-1, data)
	
print(replicate_iter(10,[]))
print(replicate_recur([],"kaiser"))
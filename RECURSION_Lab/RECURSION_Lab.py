# def replicate_iter(times, data):
# 	try:
# 		if (times <= 0):
# 			return []
# 		else:
# 			result = []
# 			for i in range(1, times+1):
# 				result.append(data)
# 		return result
		
# 	except ValueError, e:
# 		raise e

# def replicate_recur(times, data):
# 	try:
# 		if (times <= 0):
# 			return []
# 		else:
# 			return [data] + replicate_recur(times-1, data)
		
# 	except ValueError, e:
# 		raise e

# def replicate_iter(times, data):
# 	if (times <= 0):
# 		return []
# 	else:
# 		result = []
# 		for i in range(1, times+1):
# 			result.append(data)
# 		return result

# 	raise ValueError('Invalid input')

# def replicate_recur(times, data):
# 	if (times <= 0):
# 		return []
# 	return [data] + replicate_recur(times-1, data)
	
# 	raise ValueError('Invalid input')

# def replicate_iter(times, data):
# 	if (times <= 0):
# 		return []
# 	else:
# 		return [data] * times
# 	raise ValueError('Invalid input')

# def replicate_recur(times, data):
# 	if (times<= 0):
# 		return []
# 	else:
# 		return [data] + replicate_recur(times-1, data)
# 	raise ValueError('Invalid input')

# def replicate_iter(times, data):
# 	if (times <= 0):
# 		return []
# 	elif(times > 0):
# 		result = []
# 		for i in range (times+1):
# 			result.insert(i,data)
# 		return result
# 	else:
#   		raise ValueError("Invalid input")
	
# def replicate_recur(times, data):
# 	if (times <= 0):
# 		return []
# 	else:
# 		return [data] + replicate_recur(times-1, data)
	
def replicate_iter(times, data):
	try:
		if (times <= 0):
			return []
		else:
			result = []
			for i in range(1, times+1):
				result.append(data)
		return result
		
	except (TypeError, AttributeError):
		raise ValueError()

def replicate_recur(times, data):
	try:
		if (times <= 0):
			return []
		else:
			return [data] + replicate_recur(times-1, data)
		raise ValueError('This is manually raised ValueError')
		
	except (TypeError, AttributeError):
		raise ValueError()


print(replicate_iter(1,[]))
print(replicate_recur([],1))
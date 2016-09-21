def replicate_iter(times, data):
	if ((not isinstance(times, int)) or (not isinstance(data, (int, float, long, complex, str)))):
		raise ValueError("Invalid argument")
	if(times <= 0):
		return []
	else:
		result = []
		for i in range(1, times+1):
			result.append(data)
		return result

def replicate_recur(times, data):
	if ((not isinstance(times, int)) or (not isinstance(data, (int, float, long, complex, str)))):
		raise ValueError("Invalid argument")
	if (times <= 0):
		return []
	else:
		result = replicate_recur(times-1, data)
		result.append(data)

		return result
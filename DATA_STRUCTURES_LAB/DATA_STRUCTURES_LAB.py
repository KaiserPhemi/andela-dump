def manipulate_data(inp_list):
	
	if type(inp_list) != type([]):
	  return 'Only lists allowed'
	
	else:
		count_positive = sum(num >= 0 for num in inp_list)
		sum_negative = 0
		for neg_num in inp_list:
			if neg_num < 0:
				sum_negative += neg_num
		return [count_positive, sum_negative]

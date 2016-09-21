def binary_converter(num_input):
	if (num_input >= 0) and (num_input <= 255):
		return (bin(num_input)[2:])
	else:
		return "Invalid input"
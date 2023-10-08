def decompress_string(string):
	decompressed = ""
	i = 0

	while i < len(string):
		char = string[i]
		if char.isalpha():
			decompressed += char
			i += 1
		elif char.isdigit():
			char = string[i-1]
			count = ""
			while i < len(string) and string[i].isdigit():
				count += string[i]
				i += 1
			decompressed += char * (int(count) - 1)

	return decompressed


user_input = input("Введите строку (например - Y4g2ke3A3BV): ")
decompressed_string = decompress_string(user_input)
print(decompressed_string)
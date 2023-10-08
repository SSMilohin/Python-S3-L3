def compress_string(string):
	compressed = ""
	count = 1

	for i in range(len(string)-1):
		if string[i] == string[i+1]:
			count += 1
		else:
			compressed += string[i]
			if count != 1:
				compressed += str(count)
			count = 1

	compressed += string[-1]
	if count != 1:
		compressed += str(count)

	return compressed

user_input = input("Введите строку (например - YYYYggkeeeAAABV): ")
compressed_string = compress_string(user_input)
print(compressed_string)
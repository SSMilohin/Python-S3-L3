def count_chars(string):
	string = string.replace(" ", "")
	char_count = {}

	for char in string:
		if char in char_count:
			char_count[char] += 1
		else:
			char_count[char] = 1

	most_common = sorted(char_count.items(), key=lambda x: x[1], reverse=True)[:3]

	for char, count in most_common:
		print("Символ:", char, "Количество:", count)

user_input = input("Введите строку (например - Hello, world!): ")
count_chars(user_input)
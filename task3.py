def number_to_text(number):
	numbers = ["", "один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
	exceptions = ["", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"]
	tens = ["", "десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
	hundreds = ["", "сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]

	if number < 1 or number > 1000:
		return "Число должно быть в диапазоне от 1 до 1000"

	if number <= 9:
		return numbers[number]

	if number == 10:
		return tens[1]

	if number <= 19:
		return exceptions[number % 10]

	if number <= 99:
		return tens[number // 10] + " " + numbers[number % 10]

	if number <= 999:
		return hundreds[number // 100] + " " + tens[number % 100 // 10] + " " + numbers[number % 10]

	if number == 1000:
		return "тысяча"


number = int(input("Введите число от 1 до 1000: "))
text = number_to_text(number)
print("Текстовое написание числа", number, ":", text)
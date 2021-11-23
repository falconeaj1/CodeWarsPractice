def digital_root(n):
	numbers = str(n)
	total = 0
	for num in range(len(numbers)):
		total += int(numbers[num])
	if total > 9:
		total = digital_root(total)
	return total


print(digital_root(493193))

for character in 'hi':
	print(ord(character))

x = 'hello'
x += 'j'
print(x)
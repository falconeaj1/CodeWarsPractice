phoneNum = "3662277"
words = ["foo", "bar", "baz", "foobar", "emo", "car", "cap", "cat"]
# Output = ["bar, "car", "cap", "emo", "foo", "foobar"]
letterDict = {'a':'2', 'b':'2', 'c':'2', 
							'd':'3', 'e':'3', 'f':'3',
							'g':'4', 'h':'4', 'i':'4',
							'j':'5', 'k':'5', 'l':'5',
							'm':'6', 'n':'6', 'o':'6',
							'p':'7', 'q':'7', 'r':'7', 's':'7',
							't':'8', 'u':'8', 'v':'8',
							'w':'9', 'x':'9', 'y':'9', 'z':'9'}
def convertWordsToStrings(listWords, dictKey):
	numberList = []
	for word in listWords:
		wordAsNumbers = ''
		for letter in word:
			wordAsNumbers += letterDict[letter]
		numberList.append(wordAsNumbers)
	for ind in range(len(numberList)):
		print(listWords[ind], ' = ', numberList[ind])
	return numberList

def isSubstring(word, Sentence):
	for startIdx in range(len(Sentence) - len(word)):
		print('word is = ', word)
		print('Sentence[startIdx:startIdx+len(word)] = ', Sentence[startIdx:startIdx+len(word)])
		if word == Sentence[startIdx:startIdx+len(word)]:
			return True
	return False

x = convertWordsToStrings(words, letterDict)
acceptableWords = []
for ind in range(len(x)):
	if isSubstring(x[ind], phoneNum):
		acceptableWords.append(words[ind])

# convertWordsToStrings(words, letterDict)
# x = ['2','4','2','2']
print(['2','4','2'] == ['242'])
y = '2'+'4'+'3'
print(acceptableWords)
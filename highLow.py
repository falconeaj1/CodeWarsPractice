def spin_words(sentence):
    # Your code goes here
    minLength = 5
    words = sentence.split()
    newSent = []
    for word in words:
    	if len(word) >= minLength:
    		newSent.append(word[::-1])
    	else:
    		newSent.append(word)
    return " ".join(newSent)
# print(spin_words('Hello world'))

# print(set.intersection(set('abc'), set('AbBC')) == set('bB'))
words = 'Hello this   is  a   test'
x = words.split("   ")
# print(x)
x = ["M: "+str(3)]
# print(x)






def howmuch(m, n):
    # money M: m <= M <= n, 
    # M - 9*c == 1 
    # M - 7*b == 2 
    possibleValues = []
    for M in range(m, n+1):
        c = (M-1)/9
        if c == c-(c%1):
            b = (M-2)/7
            if b == b-(b%1):
                b = int(b)
                c = int(c)
                possibleValues.append(["M: "+str(M), "B: "+str(b), "C: "+str(c)])
    return possibleValues
# def howmuch(m, n):
# 	possibleValues = []
# 	for M in range(m, n+1):
# 		print('M = ', M)
# 		c = (M-1)/9
# 		print('c = ', c)
# 		if c == (c%1):
# 			b = (m-2)/7
# 			print('b = ', b)
# 			if b== (b%1):
# 				possibleValues.append(["M: "+str(M), "B: "+str(b), "C: "+str(c)])
# 	return possibleValues
print(howmuch(1,100))


def race(v1, v2, g):
	if v1 >= v2:
	    return None
	time = (round(3600 * g/ (v2-v1))) #in secs
	secs = time%60
	mins = int((time%3600 - secs)/ 60)
	hours = int((time - secs - mins*60)/3600)
	# hours = int(time - (time%1))
	# mins = (time%1) * 60
	# secs = int((mins%1) * 60)
	# mins = int(mins - (mins%1))
	return [hours, mins, secs]
    
print(race(720, 850, 37))
print((37/130 * 60)%1 * 60)


def sort_array(source_array):
	odds = sorted([a for a in source_array if a%2==1])
	new_list =[]
	current_odd = 0

	for i in range(len(source_array)):
		if source_array[i]%2 == 0:
			new_list.append(source_array[i])
		else:
			new_list.append(odds[current_odd])
			current_odd += 1

	return new_list

print(sort_array([2,3,5,1,-11,20,5,3,14]))
# WordScapes App solver by jumBop
# PERMUTATION ALGORITHM INCLUDED
# 10/12/19

def inputLetters():
	inString = input('enter letters as string: ')
	
	return inString;

# makes a list of letters w/o repeats
def makeSingles(string):
	newList = []
	for x in string:
		if (x in newList) == False:
			newList.append(x)

	return newList

# counts how many of each letter in input
def makeCountList(singles, letters):
	countList = []
	for element in singles:
		count = 0
		while element in letters:
			count = count + 1;
			letters.remove(element)
		countList.append(count)

	return countList

# generate all possible permutations
def permGen(singles, countList, results, layer):
	# check at end of recursion
	if len(results) == layer:
		outStrings.append(''.join(results))
		return
	
	for x in range(len(singles)):
		if countList[x] == 0:
			continue
		results[layer] = singles[x]
		countList[x] = countList[x] - 1
		permGen(singles, countList, results, layer + 1)
		countList[x] = countList[x] + 1 # change back after passing
		
# make a list of words with varying lengths
def differentLengths(outStrings):
	length = len(outStrings[0])
	
	while length >= 3:
		words = []
		print('length = ' + str(length))
		for word in outStrings:
			newString = ''
			for x in range(length):
				newString = newString + word[x]
			if searcher(newString, wordlist):
				if (newString in words) == False:
					print(newString)
					words.append(newString)
		print('')
		length = length - 1
		
# check wordlist for valid word
def searcher(test, wordlist):
	if test in wordlist:
		return 1
	else:
		return 0

if __name__ == '__main__':
	with open('wordlist', 'r+') as file:
		contents = file.read()
	wordlist = contents.split('\n')
	while(1):
		letters = inputLetters()
		
		if letters == 'exit()':
			break
		
		singles = makeSingles(letters)
		temp = list(letters)
		countList = makeCountList(singles, temp)
		outStrings = []
	
		results = []
		for x in letters:
			results.append('0')
	
		permGen(singles, countList, results, 0)
	
		differentLengths(outStrings)

if __name__ == '__main__':
	test = 'cat'
	with open('wordlist', 'r+') as file:
		contents = file.read()
	wordlist = contents.split('\n')

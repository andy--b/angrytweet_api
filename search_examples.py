from random import sample

def search_examples(n=1):
	terms = ['Bacon', 'Kim Kardashian', 'NY Yankees', 'Madden', 'iPhone',
		'Wallets', 'Kickball', 'Toyota', 'Playstation', 'Printer', 
		'Donald Trump', 'Winter', 'Tom Cruise', 'Basketball', 
		'Budweiser', 'Coffee', 'FIFA', 'Hillary Clinton', 'Obama',
		'Germany', '711', 'McDonalds', 'Dogs', 'Cats', 'Train', 'Ford',
		'Math Class', 'The Pope', 'CNN', 'TSwift', 'Drake', 'Brad Pitt',
		'XBOX', 'Traffic', 'Drunk', 'Neighbors', 'Eminem', 'Communism',
		'Socialism', 'Capitalism']
	random_index = sample(range(0, len(terms)), n)
	terms_list = []
	for i in random_index:
		terms_list.append(terms[i])
	return terms_list
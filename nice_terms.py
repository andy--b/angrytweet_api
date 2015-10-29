from random import sample

def nice_term(sample_size=1):
	terms = ['lovely person', 'absolute genius', 'proponent of world peace',
		'miracle worker', 'TIME Magazine Person of the Year candidate',
		'Nobel Laureate', 'disciple of Mother Teresa',
		'pacifist', 'lover of all things soft, cuddly, and warm',
		'person, who kisses their mother with that mouth,',
		'person, who probably has a secret second butt,',
		'representative of the same species as you',
		'eligible voter', 'Copernican groundbreaker',
		'future president', 'beautiful bastard', 'big ball of joy']
	random_index = sample(range(0, len(terms)), sample_size)
	nice_list = []
	for i in random_index:
		nice_list.append(terms[i])
	return nice_list
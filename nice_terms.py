from random import randint

def nice_term():
	terms = ['lovely person', 'absolute genius', 'proponent of world peace',
		'miracle worker', 'TIME Magazine Person of the Year candidate',
		'Nobel Laureate', 'disciple of Mother Teresa',
		'pacifist', 'lover of all things soft, cuddly, and warm',
		'person, who kisses their mother with that mouth,',
		'person, who probably has a secret second butt,',
		'representative of the same species as you',
		'eligible voter', 'Copernican groundbreaker',
		'future president' ]
	return terms[randint(0, len(terms)-1)]
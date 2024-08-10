# Python port of Matlab's "why" function

import random

# Words
nouns = [
    'programmer',
    'product manager',
    'engineer',
    'web developer',
    'hamster',
    'kid',
    'backend developer'
]

nominative_pronouns = [
    'I',
    'you',
    'he',
    'she',
    'they'
]

accusative_pronouns = [
    'me',
    'all',
    'her',
    'him'
]

nouned_verbs = [
    'love',
    'approval'
]

adverbs = [
    'very',
    'not very',
    'not excessively',
    'really'
]

adjectives = [
    'tall',
    'tattooed',
    'young',
    'smart',
    'rich',
    'terrified',
    'lazy',
    'good',
    'helpful'
]

articles = [
    'the',
    'some',
    'a'
]

prepositions = [
    'to',
    'from',
    'with',
    'at',
    'on',
    'in',
    'behind',
    'under'
]

proper_nouns = [
    'Tobias',
    'Mark',
    'Jane',
    'Lynn',
    'Pauline',
    'Miguel',
    'Sara',
    'Michelle',
    'Nicolas',
    'Mr. Anderson',
    'Taylor',
    'Fabien'
]

present_verbs = [
    'fool',
    'please',
    'satisfy'
]

transitive_verbs = [
    'threatened',
    'told',
    'asked',
    'helped',
    'obeyed',
    'tricked'
]

intransitive_verbs = [
    'insisted on it',
    'insisted on it... and we got cake after',
    'suggested it',
    'told me to',
    'wanted it',
    'knew it was a good idea',
    'wanted it that way',
    'really really begged for it',
    'closed their eyes and wished for it',
    'thought they would like it'
]

special_cases = [
    'why not?',
    'don\'t ask!',
    'it\'s your karma.',
    'stupid question!',
    'how should I know?',
    'can you rephrase that?',
    'it should be obvious.',
    'the devil made me do it.',
    'the computer did it.',
    'the customer is always right.',
    'in the beginning, God created the heavens and the earth...',
    'don\'t you have something better to do?',
    'it is more fun this way.',
    'because computer science isn\'t always easy.'
]

def generate():
	x = random.randrange(1, 10)
	if x == 1:
	  	return random.choice(special_cases).capitalize()
	if x == 2:
	   	return phrase().capitalize()
	else:
	   	return sentence().capitalize()

def phrase():
	x = random.randrange(1, 3)
	if x == 1:
		return 'for the ' + random.choice(nouned_verbs) + ' ' + prepositionalPhrase() + '.'
	if x == 2:
		return 'to ' + random.choice(present_verbs) + ' ' + object() + '.'
	else:
		return 'because ' + sentence()

def prepositionalPhrase():
	x = random.randrange(1, 3)
	if x == 1:
		return random.choice(prepositions) + ' ' + random.choice(articles) + ' ' + nounPhrase()
	if x == 2:
		return random.choice(prepositions) + ' ' + random.choice(proper_nouns)
	else:
		return random.choice(prepositions) + ' ' + random.choice(accusative_pronouns)

def sentence():
	return subject() + ' ' + predicate() + '.'

def subject():
	x = random.randrange(1, 4)
	if x == 1:
		return random.choice(proper_nouns)
	if x == 2:
		return random.choice(nominative_pronouns)
	else:
		return random.choice(articles) + ' ' + nounPhrase()

def nounPhrase():
	x = random.randrange(1, 4)
	if x == 1:
		return random.choice(nouns)
	if x == 2:
		return adjectivePhrase() + ' ' + nounPhrase()
	else:
		return adjectivePhrase() + ' ' + random.choice(nouns)

def adjectivePhrase():
	x = random.randrange(1, 5)
	if x == 3:
		return random.choice(adjectives)
	if x == 4:
		return adjectivePhrase() + ' and ' + adjectivePhrase()
	else:
		return random.choice(adverbs) + ' ' + random.choice(adjectives)

def predicate():
	x = random.randrange(1, 3)
	if x == 1:
		return random.choice(transitive_verbs) + ' ' + object()
	else:
		return random.choice(intransitive_verbs)

def object():
	x = random.randrange(1, 10)
	if x == 1:
		return random.choice(accusative_pronouns)
	else:
		return random.choice(articles) + ' ' + nounPhrase()


print(generate())
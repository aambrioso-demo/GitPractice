# The main program for the Git exercise

quote = 'Computer science inverts the normal. In normal science,\nyou\'re given a world, and your job is to find out the rules.\nIn computer science, you give the computer the rules, and it creates the world.'

import random

def num(length):
    return random.randint(0, length-1)

# Checks that adjective module is set up.
# If it is not set up adjectives default to the original quote.
try:
    import adjectives
    length = len(adjectives.adj)
    adj1 = adjectives.adj[num(length)]
    adj2 = adjectives.adj[num(length)]
    print(adj1, adj2)

except:
    print('Using default adjectives.')
    adj1 = 'Computer'
    adj2 = 'normal'

try:
	import nouns
	length = len(nouns.noun)
	noun1 = nouns.noun[num(length)]
	noun2 = nouns.noun[num(length)]
	noun3 = nouns.noun[num(length)]
	noun4 = nouns.noun[num(length)]
	noun5 = nouns.noun[num(length)]
	noun6 = nouns.noun[num(length)]

except:
    print('Using default nouns')
    noun1 = 'Science'
    noun2 = 'normal'
    noun3 = 'world'
    noun4 = 'job'
    noun5 = 'rules'
    noun6 = 'computer'


try:
	import verbs
	length = len(verbs.verb)
	verb1 = verbs.verb[num(length)]

except:
    print('Using the default verb.')
    verb1 = 'creates'

# Print out quote with random words filled in.
quote_with_blanks = f'{adj1} {noun1} inverts the {noun2}. In {adj2} {noun1},\nyou\'re given a {noun3}, and your {noun4} is to find out the {noun5}. \nIn {adj1} {noun1}, you give the {noun6} the {noun5}, and it {verb1} the {noun3}.'
print('\n')
print('*' * 70)
print(quote_with_blanks)
print('*' * 70)
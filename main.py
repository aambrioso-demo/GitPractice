# The main program for a Git exercise.   

quote = 'Computer science inverts the normal. In normal science,\n \
you\'re given a world, and your job is to find out the rules.\n \
In computer science, you give the computer the rules, and it creates the world.'

import random

def num(length):
    return random.randint(0, length-1)

# Checks that adjective module is set up.
# If it is not set up adjectives default to the original quote.
try:
    import adjectives
    length = len(adjectives.adjs)
    adj1 = adjectives.adjs[num(length)]
    adj1 = adj1[0].upper() + adj1[1:] # in order to capitalize the first letter of the sentence.
    adj2 = adjectives.adjs[num(length)]
    
except:
    print('Using default adjectives.')
    adj1 = 'Computer'
    adj2 = 'normal'
# Checks that the noun module is set up.
# if it is not set up the nouns default to those in the original quote.
try:
	import nouns
	length = len(nouns.nouns)
	noun1 = nouns.nouns[num(length)]
	noun2 = nouns.nouns[num(length)]
	noun3 = nouns.nouns[num(length)]
	noun4 = nouns.nouns[num(length)]
	noun5 = nouns.nouns[num(length)]
	noun6 = nouns.nouns[num(length)]

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
	length = len(verbs.verbs)
	verb1 = verbs.verbs[num(length)]

except:
    print('Using the default verb.')
    verb1 = 'creates'

# Print out quote with random words filled in.
quote_with_blanks = f'{adj1} {noun1} inverts the {noun2}.\n\
In {adj2} {noun1}, you\'re given a {noun3}, and your {noun4} is to find out the {noun5}.\n\
In {adj1} {noun1}, you give the {noun6} the {noun5}, and it {verb1} the {noun3}.'
print('*' * 70)
print(quote_with_blanks)
print('*' * 70)
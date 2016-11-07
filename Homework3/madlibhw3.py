# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns - adjectives, verbs, adverbs, plural noun
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens) - done
# 1) Print the new text
print("START*******")

import nltk 
from nltk.book import *
from nltk import bigrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import word_tokenize, sent_tokenize
import random #one of these is printing all the texts, is this ok?

# fname = "austen-sense.txt"
# f = open(fname, 'r')
# para = f.read()

para = text2[:151]

tokens = nltk.word_tokenize(para)
print("TOKENS")
print(tokens[:151])

tagged_tokens = nltk.pos_tag(tokens)
tagged_tokens = tagged_tokens[:151] # gives us a tagged list of tuples
print("TAGGED TOKENS")
print(tagged_tokens)


tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","RB":"an adverb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"RB":.1, "JJ":.1}

def spaced(word):
	if word in [",", ".", "?", "!", ":", "[", "]"]:
		return word
	else:
		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
		final_words.append(spaced(word))
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word))
print
print ("".join(final_words))

print("\n\nEND*******")

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
from nltk.book import text2
import random

tokens = text2[:151] #only need first 150
print
print("First 150 tokens:")
print(tokens)

tagged_tokens = nltk.pos_tag(tokens) 
tagged_tokens = tagged_tokens[:151] # gives us a tagged list of tuples

#parts of speech and their probabilities
tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","RB":"an adverb","JJ":"an adjective"}
substitution_probabilities = {"NN":.15,"NNS":.15,"VB":.1,"RB":.1, "JJ":.1}

#dont add space to punctuation
def spaced(word):
	if word in [",", ".", "?", "!", ":", "[", "]"]:
		return word
	else:
		return " " + word

#for mad lib output 
final_words = []

for (word, tag) in tagged_tokens: 
	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]: #decides to choose or skip each part of speech
		final_words.append(spaced(word)) #adds normal text
	else:
		new_word = input("Please enter %s:\n" % (tagmap[tag]))
		final_words.append(spaced(new_word)) #adds user inputted word 
print
print ("".join(final_words)) #both if and else funnel to final_words, then joined them together 

print("\n\nEND*******")

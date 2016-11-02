# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import nltk 
from nltk.book import *
from nltk import bigrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import word_tokenize, sent_tokenize
import random #one of these is printing all the texts, is this ok?

print("\n\n")
print("type of text 2 is ", type(text2))
print("Length of ",text2,"is",len(text2))
print("Unique tokens in",text2,"are: ",len(set(text2)))


tokens = nltk.word_tokenize(text2)
print("TOKENS")
print(tokens)
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
print("TAGGED TOKENS")
print(tagged_tokens)
if debug:
	print ("First few tagged tokens are:")
	for tup in tagged_tokens[:5]:
		print (tup)


# sentences = sent_tokenize(text2)
# print ("Type of sentences is", type(sentences))
print("\n\n")




# tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective"}
# substitution_probabilities = {"NN":.1,"NNS":.2,"VB":.25,"JJ":.25}

# for i in sentences:
# 	print(i)

print("\n\nEND*******")

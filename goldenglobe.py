import json
import nltk 
import re, string
regex = re.compile('[%s]' % re.escape(string.punctuation))
from pprint import pprint
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import *
from nltk import bigrams
from nltk.tokenize import RegexpTokenizer
from nltk.collocations import *
from collections import Counter

def remove_punct(string):
	string=regex.sub(' ', string)
	return string




data = []
with open('/Users/MatthewSchley/Downloads/gg2013.json') as f:
    for line in f:
        data.append(json.loads(line))

# print data
# print data[0]["text"]
corpus = []
for tweet in data[0]: 
	text = tweet["text"].lower()	
	text = remove_punct(text)
	#tokens = tokenize(text)
	if "best actor in a motion picture drama" in text:
		corpus.append(text)
	#	print "\n"
	# corpus.append(text)
	# print tokens

#print corpus
token_array = []
bigram_array = []
bigram_array2 = []
for x in range(0,len(corpus)):
	#print corpus[x]
	sentence = corpus[x]
	tokens = nltk.word_tokenize(sentence)
	bigrams = nltk.bigrams(sentence)
	token_array.append(tokens)
	pairs = [ ", ".join(pair) for pair in nltk.bigrams(tokens)]	
	print bigrams
	bigram_array.append(pairs)
	words = re.findall('\w+', sentence)
	bigram_array2.append(Counter(zip(words,words[1:])))

stopset = set(stopwords.words('english'))

final_array = []
no_common_words_array = []
#print len(token_array)
for x in range(0,len(token_array)):
	#print corpus[x]
	token_list = token_array[x]
	for y in range(0,len(token_list)):
		one_token = token_list[y]
		temp_array = []
		if one_token not in stopset:
			####print one_token	
			final_array.append(one_token)
			#print one_token
			#temp_array.append(one_token)
			#final_array.append(temp_array[0])
			#no_common_words = (token_list)
			#no_common_words_array.append(no_common_words)


###print final_array

fdist = FreqDist(final_array)
# print fdist.most_common(100)


#for x in range(0,len(bigram_array)):
#	print bigram_array[x]
#	print "\n"

fdist1 = nltk.FreqDist(bigram_array2)
print fdist1.most_common(100)

bigram_measures = nltk.collocations.BigramAssocMeasures()
finder = BigramCollocationFinder.from_words(bigrams)
final = finder.nbest(bigram_measures.pmi, 10) 

#print final


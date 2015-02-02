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
	if  in text:
		corpus.append(text)
	#	print "\n"
	# corpus.append(text)
	# print tokens

#print corpus
token_array = []
bigram_array = []
for x in range(0,len(corpus)):
	#print corpus[x]
	sentence = corpus[x]
	tokens = nltk.word_tokenize(sentence)
	bigrams = nltk.bigrams(sentence)
	token_array.append(tokens)
	bigram_array.append(bigrams)
	pairs = [ " ".join(pair) for pair in nltk.bigrams(tokens)]	
	#print pairs
	bigram_array.append(pairs)

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
print fdist.most_common(100)


#for x in range(0,len(bigram_array)):
	#print bigram_array[x]


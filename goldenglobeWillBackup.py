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

def remove_punctuation(string):
	string=regex.sub(' ', string)
	return string

def removeIgnored(phrase):
	words = phrase.split(' ')
	stopset = set(stopwords.words('english'))
	stopset.add('best')
	stopset.add('golden')
	stopset.add('globes')
	stopset.add('goldenglobes')
	stopset.add('goldenglobe')
	stopset.add('rt')
	stopset.add('actor')
	stopset.add('actress')
	for i in range(0,len(words)):
		stopset.add(words[i])
	return stopset

def findTopTweets(award):
	print "     Searching for top tweets..."
	data = []
	with open('gg2013.json') as f:
	    for line in f:
	        data.append(json.loads(line))

	# this code block creates our corpus of relevant tweets - an array of tweet objects
	corpus = []
	for tweet in data[0]: 
		text = tweet["text"].lower()	
		text = remove_punctuation(text)
		tokenNotFound = False
		awardTokens = nltk.word_tokenize(award)
		for token in awardTokens:
			if text.find(token)==-1:
				tokenNotFound = True
		if tokenNotFound is False:
			# print awardTokens
			corpus.append(text)


	# this code block turns tweets into unigrams and bigrams and then stores them in token_array and bigram_array2
	token_array = []
	bigram_array = []
	bigram_array2 = []
	for x in range(0,len(corpus)):
		#print corpus[x]
		sentence = corpus[x]
		tokens = nltk.word_tokenize(sentence)
		bigrams = nltk.bigrams(sentence)
		token_array.append(tokens)
		words = re.findall('\w+', sentence)
		temp = zip(words,words[1:]) # originally had Counter() wrapped around zip(...)
		bigram_array2.append(temp)


	stopset = removeIgnored(award)

	final_array = [] # this array will store all unigrams 
	no_common_words_array = []
	for x in range(0,len(token_array)):
		token_list = token_array[x]
		for y in range(0,len(token_list)):
			one_token = token_list[y]
			temp_array = []
			if one_token not in stopset:
				####print one_token	
				final_array.append(one_token)

	all_bigrams_array = [] # this array will store all bigrams
	for x in range(0,len(bigram_array2)):
		bigram_collection = bigram_array2[x]
		for y in range(0,len(bigram_collection)):
			one_bigram = bigram_collection[y]
			temp_array = []
			if one_bigram[0] not in stopset:
				if one_bigram[1] not in stopset:
					all_bigrams_array.append(one_bigram)

	fdistUnigram = FreqDist(final_array)
	topUni = fdistUnigram.most_common(10)
	fdistBigram = nltk.FreqDist(all_bigrams_array)
	topBi = fdistBigram.most_common(10)
	print topBi
	return topUni,topBi

def findWinner(topUnigrams, topBigrams, nominees):
	for i in range(0,len(topUnigrams)):
		for j in range (0,len(nominees)):
			biPart1 = (topBigrams[i][0])[0]
			biPart2 = (topBigrams[i][0])[1]
			uni = topUnigrams[i][0]
			nominee = nominees[j].lower()
			if nominee.find(biPart1)!= -1 or nominee.find(biPart2)!=-1:
				return nominees[j]
				break


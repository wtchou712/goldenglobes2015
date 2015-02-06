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

	stopset = removeIgnored(award)

	# this code block creates our corpus of relevant tweets - an array of tweet objects
	bigram_array = []
	unigram_array = []
	for tweet in data[0]: 
		tweetText = tweet["text"].lower()	
		tweetText = remove_punctuation(tweetText)
		tokenNotFound = False
		awardTokens = nltk.word_tokenize(award)
		for token in awardTokens:
			if tweetText.find(token)==-1:
				tokenNotFound = True
		if tokenNotFound is False:
			#add to array of unigrams
			tweetTokens = nltk.word_tokenize(tweetText)
			for tok in tweetTokens:#add appropriate unigrams
				if tok not in stopset:
					unigram_array.append(tok)

			#add to array of bigams
			words = re.findall('\w+', tweetText) #seperate the words
			bigrams = zip(words, words[1:]) #create the bigrams
			for bi in bigrams:
				if bi[0] not in stopset and bi[1] not in stopset:
					bigram_array.append(bi)

	fdistUnigram = FreqDist(unigram_array)
	topUni = fdistUnigram.most_common(10)
	fdistBigram = nltk.FreqDist(bigram_array)
	topBi = fdistBigram.most_common(10)
	# print topUni
	# print topBi
	return topUni,topBi

def findWinner(topUnigrams, topBigrams, nominees):
	singleWordNom = False
	for nom in nominees: #search nominees to see if any are single words
		checkNom = nltk.word_tokenize(nom)
		if len(checkNom)!=0:
			singleWordNom= True
			break
	for i in range(0,len(topUnigrams)):
		for j in range (0,len(nominees)):
			biPart1 = (topBigrams[i][0])[0]
			biPart2 = (topBigrams[i][0])[1]
			uni = topUnigrams[i][0]
			nominee = nominees[j].lower()
			if singleWordNom:#use unigram search if single words nominee
				if nominee.find(uni)!=-1:
					return nominees[j]
					break
			else:
				if nominee.find(biPart1)!= -1 or nominee.find(biPart2)!=-1:
					return nominees[j]
					break

			


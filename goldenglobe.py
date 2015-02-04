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


		directory = {'Ben Affleck': 'Argo', 'Kathryn Bigelow' : "Zero Dark Thirty", 'Ang Lee': 'Life of Pi', 'Steven Speilberg': 'Lincoln',
				  'Quentin Tarantino': 'Django Unchained', 'Jessica Chastain':'Zero Dark Thirty', 'Marion Cotillard': 'Rust and Bone',
				  'Helen Mirren':'Hitchcock', 'Naomi Watts': 'The Impossible', 'Rachel Weisz': 'The Deep Blue Sea', 'Daniel Day-Lewis': 'Lincoln',
				  'Richard Gere': 'Arbitage', 'John Hawkes': 'The Sessions', 'Joaquin Phoenix': 'The Master', 'Denzel Washington':'Flight',
				  'Jack Black': 'Bernie', 'Bradley Cooper': 'Silver Linings Playbook', 'Hugh Jackman': 'Les Miserables', 'Ewan McGregor': 'Salmong Fishing in the Yemen', 
				  'Bill Murray': 'Hyde Park on Hudson', 'Emily Blunt': 'Salmon Fishing in the Yemen', 'Judi Dench': 'The Best Exotic Marigold Hotel',
				  'Jennifer Lawrence':'Silver Linings Playbook', 'Maggie Smith':'Quartet', 'Meryl Streep': 'Hope Springs', 'Amy Adams': 'The Master',
				  'Sally Field':'Lincoln', 'Anne Hathaway':'Les Miserables', 'Helen Hunt':'The Sessions', 'Nicole Kidman':'The Paperboy', 'Alan Arkin':'Argo', 
				  'Leonardo DiCaprio':,'Django Unchained', 'Philip Seymour Hoffman':'The Master', 'Tommy Lee Jones':'Lincoln','Christoph Waltz':'Django Unchained',
				  'Mark Boal':'Zero Dark Thirty', 'Tony Kushner':'Lincoln', "David O'Russell":'Silver Linings Playbook', 'Chris Terrio':'Argo'
				  'For You': 'music and lyrics by Monty Powell, Keith Urban in "Act of Valor"', 'Not Running Anymore': 'music and lyrics by Jon Bon Jobi in "Stand Up Guys"', 
				  'Safe & Sound' : 'music and lyrics by Taylor Swift, John Paul White, Joy Williams, T Bone Burnett in "The Hunger Games"',
				  'Skyfall': 'music and lyrics by Adele and Paul Epworth in "Skyfall"', 'Suddenly':'music by Claude-Michel Stchonberg and lyrics by Herbert Kretzmer and Alain Boublil in "Les Miserables"',
				  'Mychael Danna': 'Life of Pi', 'Alexandre Desplat':'Argo', 'Dario Marianelli':'Anna Karenina', 'Tom Tykwer, Johnny Klimek and Reinhold Heil':'Cloud Atlas',
				  'John Williams':'Lincoln', 'Steve Buscemi':'Boardwalk Empire', 'Bryan Cranston':'Breaking Bad', 'Jeff Daniels':'The Newsroom',
				  'Jon Hamm':'Mad Men', 'Damian Lewis':'Homeland', 'Zooey Deschanel':'New Girl', 'Julia Louis-Dreyfus':'Veep', 'Lena Dunham':'Girls', 
				  'Tina Fey':'30 Rock', 'Amy Poehler':'Parks and Recreation', 'Alex Baldwin':'30 Rock', 'Don Cheadle':'House of Lies', 
				  'Louis C.K.':'Louie', 'Matt LeBlanc':'Episodes', 'Jim Parsons':'The Big Bang Theory', 'Nicole Kidman':'Hemingway & Gellhorn', 
				  'Jessica Lange':'American Horror Story:Asylum', 'Sienna Miller':'The Girl', 'Julianna Moores':'Game Change', 'Sigourney Weaver':'Political Animals', 
				  'Kevin Costner':'Hatfields & McCoys', 'Benedict Cumberbatch':'Sherlock(Masterpiece)', 'Woody Harrelson':'Game Change', 'Toby Jones':'The Girl', 
				  'Clive Owen':'Hemingway & Gellhorn', 'Hayden Panettiere':'Nashville', 'Archie Panjabi':'The Good Wife', 'Sarah Paulson':'Game Change',
				  'Maggie Smith':'Downtown Abbey:Season 2', 'Sofia Vergara':'Modern Family', 'Max Greenfield':'New Girl', 'Ed Harris':'Game Change', 'Danny Huston':'Magic City', 
				  'Eric Stonestreet':'Modern Family'}

MPDrama = ["Argo", "Django Unchained", "Life of Pi", "Lincoln", "Zero Dark Thirty"]
MPMusicComedy = ["The Best Exotic Marigold Hotel", "Les Miserables", "Moonrise Kingdom", "Salmon Fishing in the Yemen", "Silver Linings Playbook"]
MPDirector = ["Ben Affleck", "Kathryn Bigelow", "Ang Lee", "Steven Steilberg", "Quentin Tarantino"]
MPActressDrama = ["Jessica Chastain", "Marion Cotillard", 'Helen Mirren', 'Naomi Watts', 'Rachel Weisz']
MPActorDrama = ['Daniel Day-Lewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington']
MPActorMusicComedy = ['Jack Black', 'Bradley Cooper', 'Hugh Jackman', 'Ewan McGregor', 'Bill Murray']
MPActressMusicComedy = ['Emily Blunt', 'Judi Dench', 'Jennifer Lawrence', 'Maggie Smith', 'Meryl Streep']
MPSupportingActor = ['Alan Arkin', 'Leonardo DiCaprio', 'Philip Seymour Hoffman', 'Tommy Lee Jones', 'Christoph Waltz']
MPScreenplay = ['Mark Boal', 'Tony Kushner', "David O'Russell", 'Quentin Tarantino', 'Chris Terrio']
MPForeign = ['Amour','A Royal Affair', 'The Intouchables', 'Kon-Tiki', 'Rust and Bone']
MPAnimated = ['Rise of the Guardians', 'Brave', 'Frankenweenie', 'Hotel Transylvania', 'Wreck-It Ralph']
MPSong = ['For You', 'Not Running Anymore', 'Safe & Sound', 'Skyfall', 'Suddenly']
MPScore = ['Mychael Danna', 'Alexandre Desplat', 'Dario Marianelli', 'Tom Tykwer, Johnny Klimek, Reinhold Heil', 'John Williams']

TVMusicComedy = ['The Big Bang Theory', 'Episodes' , 'Girls', 'Modern Family', 'Smash']
TVDrama = ['Breaking Bad', 'Boardwalk Empire', 'Downtown Abbey', 'Homeland', 'The Newsroom']
TVActressDrama = ['Connie Britton', 'Glenn Close', 'Claire Danes', 'Michelle Dockery', 'Julianna Margulies']
TVActorDrama = ['Steve Buscemi', 'Bryan Cranston', 'Jeff Daniels', 'Jon Hamm', 'Damian Lewis']
TVActressComedy = ['Zooey Deschanel', 'Julia Louis-Dreyfous', 'Lena Dunham', 'Tina Fey', 'Amy Poehler']
TVActorComedy = ['Alec Baldwin', 'Don Cheadle', 'Louis C.K.', 'Matt LeBlanc', 'Jim Parsons']
TVMiniseries = ['Game Change', 'The Girl', 'Hatfields & McCoys', 'The Hour', 'Political Animals']
TVActressMiniseries = ['Nicole Kidman', 'Jessica Lange', 'Sienna Miller', 'Julianne Moore', 'Sigourney Weaver']
TVActorMiniSeries = ['Kevin Costner', 'Benedict Cumberbatch', 'Woody Harrelson', 'Toby Jones', 'Clive Owen']
TVSupportingActress = ['Hayden Panettiere', 'Archie Panjabi', 'Sarah Paulson' , 'Maggie Smith', 'Sofia Vergara']
TVSupportingActor = ['Max Greenfield', 'Ed Harris', 'Danny Huston', 'Mandy Patinkin', 'Eric Stonestreet']


def remove_punct(string):
	string=regex.sub(' ', string)
	return string

print "================================================="
print "\n"
data = []
with open('gg2013.json') as f:
    for line in f:
        data.append(json.loads(line))

# this code block creates our corpus of relevant tweets - an array of tweet objects
corpus = []
for tweet in data[0]: 
	text = tweet["text"].lower()	
	text = remove_punct(text)
	#tokens = tokenize(text)
	if "best actor in a motion picture comedy" in text:
		corpus.append(text)

	#	print "\n"
	# corpus.append(text)
	# print tokens

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
	#pairs = [ ", ".join(pair) for pair in nltk.bigrams(tokens)]	
	#print bigrams
	#bigram_array.append(pairs)
	words = re.findall('\w+', sentence)
	temp = zip(words,words[1:]) # originally had Counter() wrapped around zip(...)
	bigram_array2.append(temp)

stopset = set(stopwords.words('english')) # this is the creation of our stopset -- words we don't want to include
stopset.add('best')
stopset.add('golden')
stopset.add('globes')
stopset.add('goldenglobes')
stopset.add('goldenglobe')
stopset.add('rt')
stopset.add('actor')
stopset.add('motion')
stopset.add('picture')
stopset.add('comedy')
stopset.add('musical')

final_array = [] # this array will store all unigrams 
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

all_bigrams_array = [] # this array will store all bigrams
for x in range(0,len(bigram_array2)):
	#print corpus[x]
	bigram_collection = bigram_array2[x]
	#print bigram_collection
	#print "\n"
	for y in range(0,len(bigram_collection)):
		one_bigram = bigram_collection[y]
		#print one_token
		temp_array = []
		# ADD CODE FOR STOPSET USING IF STATEMENT BELOW... need to check a and b in tuple (a,b) for stopset match
		if one_bigram[0] not in stopset:
			if one_bigram[1] not in stopset:
			####print one_token	
				all_bigrams_array.append(one_bigram)

print "UNIGRAM FREQUENCY OUTPUT"
#print all_bigrams_array  # this is an array containing all bigrams... 
fdist = FreqDist(final_array)
print fdist.most_common(20)
print "================================================="
print "\n"
print "BIGRAM FREQUENCY OUTPUT"
# This is the frequency counter for bigrams... all_bigrams_array is a list of all bigrams from queried tweets 
fdist1 = nltk.FreqDist(all_bigrams_array)
print fdist1.most_common(20)
print "================================================="

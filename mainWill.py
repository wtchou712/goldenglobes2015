from goldenglobeWill import findTopTweets
from goldenglobeWill import findWinner
from goldenglobeWill import remove_punctuation

directory = {'Ben Affleck': 'Argo', 'Kathryn Bigelow' : "Zero Dark Thirty", 'Ang Lee': 'Life of Pi', 'Steven Speilberg': 'Lincoln',
		  'Quentin Tarantino': 'Django Unchained', 'Jessica Chastain':'Zero Dark Thirty', 'Marion Cotillard': 'Rust and Bone',
		  'Helen Mirren':'Hitchcock', 'Naomi Watts': 'The Impossible', 'Rachel Weisz': 'The Deep Blue Sea', 'Daniel Day-Lewis': 'Lincoln',
		  'Richard Gere': 'Arbitage', 'John Hawkes': 'The Sessions', 'Joaquin Phoenix': 'The Master', 'Denzel Washington':'Flight',
		  'Jack Black': 'Bernie', 'Bradley Cooper': 'Silver Linings Playbook', 'Hugh Jackman': 'Les Miserables', 'Ewan McGregor': 'Salmong Fishing in the Yemen', 
		  'Bill Murray': 'Hyde Park on Hudson', 'Emily Blunt': 'Salmon Fishing in the Yemen', 'Judi Dench': 'The Best Exotic Marigold Hotel',
		  'Jennifer Lawrence':'Silver Linings Playbook', 'Maggie Smith':'Quartet', 'Meryl Streep': 'Hope Springs', 'Amy Adams': 'The Master',
		  'Sally Field':'Lincoln', 'Anne Hathaway':'Les Miserables', 'Helen Hunt':'The Sessions', 'Nicole Kidman':'The Paperboy', 'Alan Arkin':'Argo', 
		  'Leonardo DiCaprio':'Django Unchained', 'Philip Seymour Hoffman':'The Master', 'Tommy Lee Jones':'Lincoln','Christoph Waltz':'Django Unchained',
		  'Mark Boal':'Zero Dark Thirty', 'Tony Kushner':'Lincoln', "David O'Russell":'Silver Linings Playbook', 'Chris Terrio':'Argo',
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

MPDrama = ["Lincoln", "Django Unchained", "Life of Pi", "Argo", "Zero Dark Thirty"]
MPMusicComedy = ["The Best Exotic Marigold Hotel", "Les Miserables", "Moonrise Kingdom", "Salmon Fishing in the Yemen", "Silver Linings Playbook"]
MPDirector = ["Ben Affleck", "Kathryn Bigelow", "Ang Lee", "Steven Steilberg", "Quentin Tarantino"]
MPActressDrama = ["Jessica Chastain", "Marion Cotillard", 'Helen Mirren', 'Naomi Watts', 'Rachel Weisz']
MPActorDrama = ['Daniel Day-Lewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington']
MPActorMusicComedy = ['Jack Black', 'Bradley Cooper', 'Hugh Jackman', 'Ewan McGregor', 'Bill Murray']
MPActressMusicComedy = ['Emily Blunt', 'Judi Dench', 'Jennifer Lawrence', 'Maggie Smith', 'Meryl Streep']
MPSupportingActress = ['Amy Adams', 'Sally Field', 'Anne Hathaway', 'Helen Hunt', 'Nicole Kidman']
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

allNominees = [MPDrama, MPMusicComedy, MPDirector, MPActressDrama, MPActorDrama, MPActorMusicComedy, MPActressMusicComedy, MPSupportingActress, MPSupportingActor, MPScreenplay, MPForeign,
			   MPAnimated, MPSong, MPScore, TVMusicComedy, TVDrama, TVActressDrama, TVActorDrama, TVActressComedy, TVActorComedy, TVMiniseries, TVActressMiniseries,
			   TVActorMiniSeries,TVSupportingActress, TVSupportingActor]
awardsList = ['Best Motion Picture - Drama', 'Best Motion Picture - Musical or Comedy', 'Best Director - Motion Picture', 'Best Actress in a Motion Picture - Drama',
			  'Best Actor in a Motion Picture - Drama', 'Best Actor in a Musical or Comedy - Motion Picture', 'Best Actress in a Musical or Comedy - Motion Picture',
			  'Best Supporting Actress - Motion Picture', 'Best Supporting Actor - Motion Picture', 'Best Screenplay - Motion Picture', 'Foreign Film - Motion Picture', 
			  'Best Animated Film - Motion Picture', 'Best Original Song - Motion Picture', 'Best Original Score - Motion Picture', 'Best TV Comedy or Musical', 'Best TV Drama',
			  'Best Actress in a TV Drama', 'Best Actor in a TV Drama', 'Best Actress in a TV Comedy or Musical', 'Best Actor in a TV Comedy or Musical', 'Best Miniseries or TV Movie',
			  'Best Actress in a Miniseries or TV Movie', 'Best Actor in a Miniseries or TV Movie', 'Best Supporting Actress in a TV Show, Miniseries or TV Movie', 
			  'Best Supporting Actor in a TV Show, Miniseries or TV Movie']


def searchAward(awardChoice):
	# print "you entered", awardChoice
	print "Searching for the winner of " + awardsList[awardChoice-1]

	if awardChoice is 12: #animated film
		results=findTopTweets(remove_punctuation(("Animated Film").lower()))
		winner = findWinner(results[0], results[1], allNominees[awardChoice-1])
	elif awardChoice is 11: #foreign film
		results=findTopTweets(remove_punctuation(('Foreign Film').lower()))
		winner = findWinner(results[0], results[1], allNominees[awardChoice-1])	
	else:
		results=findTopTweets(remove_punctuation((awardsList[awardChoice-1]).lower()))
		winner = findWinner(results[0], results[1], allNominees[awardChoice-1])

	# print allNominees[awardChoice-1]
	if winner in directory:
		print "The award for " + awardsList[awardChoice-1] + " goes to " + winner + " in " + directory[winner]
	else: 
		print "The award for " + awardsList[awardChoice-1] + " goes to " + str(winner)



for i in range(0, len(awardsList)):
	print str(i+1) + ": " + awardsList[i]  
# awardChoice = int(raw_input("Choose the number of award you want to see: "))
# searchAward(awardChoice)

print "Searching all..."
for index in range(1,26):
	searchAward(index)




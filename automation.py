# Still under development. Created by Edmond Tsoi @ 2019. 
# Python v3.7.3
import facebook
import random
import time
from facepy import GraphAPI
from time import sleep

# https://developers.facebook.com/tools/explorer <= where you can get access token.

api = "" # input api
page_token_01 = "" # input page_token

# Non-expiring tokens for Elizabeth Whites and Alexander Maher.
ewhites = "" # input token for bots
amaher = "" # input token for bots

bots = [ewhites, amaher]

# TODO: Make more extensive use of emojis!!
comments = ["sure", "LOL", ":)", "<3", "wait what?", "you gotta be kidding me", "totally agree", "can't agree more ", "LMAO"]

duration = [300.0, 400.0, 800.0, 600.0, 30.0]
group_id = "363346444370961"

messages = [
			"My mom said that if I don't pass this pre-calc test, she is gonna sell all my toys.....😢😢😭", 
			"Meet my friend Elliot. He is a trader from NY with a networth of over 300 million dollars🤑🤑....",
			"Sometimes I keep thinking to myself -- Who the hell first came up with the idea of Facebook? Mark Zukerberg must be a genius to think about this 👍",
			"One day I would surpass Elon Musk to change the world completely with electric cars 🚕🚗🚙 ",
			"Sweetwaters on Plymouth is definitely my favorite study spot😶😶",
			"I love No Thai. Their potato curry is exceptional🤤🤤",
			"Subleasing an apartment from mid July - September. Located at 1770 Broadway. Message me if you are interested😉",
			"My first, big goal upon graduation would be to pay off my college loans so that I can finally have some savings.💪",
			"I love Avengers!!!! Go Marvel!",
			"The world is strange sometimes. I have a friend who went to college, who clearly understood what Bitcoin was, and still invested in Bitcoin 😵😵..",
			"Suns out guns out 🤘🤘🤘",
			"UMich is def my dream school...",
			"Go invest in 5G stocks. Trust me, it is gonna be a huge thing in the next 10 years or even more.",
			"Is Lebron James or Michael Jordan the GOAT???😶😶",
			"Kawhi Leonard is leaving Toronto Raptors to join the Lakers.....",
			"Did you guys know there were 3 million people protesting in Hong Kong??....That number is scary....",
			"I am glad that Hong Kong people are brave enough to stand out to fight for true democracy... amazing!🤘",
			"Alright, its time to go to bed :)",
			"Can someone explain to me what an inscribed angle is? I am confused :(",
			"Selling two football seasonal tickets. DM me if interested",
			"Leg days are hard, but please don't skip leg days.",
			"Is anything going to be in New York this summer? Hit me up!",
			"The rent in California is absolutely insane....I don't think I will be able to have spare money after paying tax and rent.",
			"Ann Arbor is such a good place to live at.",
			"Siberian cats are the most cat affable breed in the world!!",
			"Go blue!!!!!",
			"How tall is Mo Wagner?",
			"Drinking water will help you lose weight because it speeds up your metabolism",
			"It's time to wake up....OMG I don't want to go to class...",
			"I cant imagine myself living in an apartment without AC. How am I gonna survive in the summer when it is 90 degrees?",
			"One thing I really want to do this summer is to travel in Europe.",
			"Happy birthday to me!",
		   ]

# Some inspiration below... (Adopted from http://pythonfiddle.com/random-sentence-generator/)
s_nouns = ["A dude", "My mom", "The king", "Some guy", "A cat with rabies", "A sloth", "Your homie", "This cool guy my gardener met yesterday", "Superman"]
p_nouns = ["These dudes", "Both of my moms", "All the kings of the world", "Some guys", "All of a cattery's cats", "The multitude of sloths living under your bed", "Your homies", "Like, these, like, all these people", "Supermen"]
s_verbs = ["eats", "kicks", "gives", "treats", "meets with", "creates", "hacks", "configures", "spies on", "retards", "meows on", "flees from", "tries to automate", "explodes"]
p_verbs = ["eat", "kick", "give", "treat", "meet with", "create", "hack", "configure", "spy on", "retard", "meow on", "flee from", "try to automate", "explode"]
infinitives = ["to make a pie.", "for no apparent reason.", "because the sky is green.", "for a disease.", "to be able to make toast explode.", "to know more about archeology."]

def sing_sen_maker():
    '''Makes a random senctence from the different parts of speech. Uses a SINGULAR subject'''
    print(random.choice(s_nouns) + " " + random.choice(s_verbs) + " " + random.choice(s_nouns).lower() or random.choice(p_nouns).lower() + " " + random.choice(infinitives))

def postMessage(token_in, text, link_in = ""):
	g = GraphAPI(token_in)
	g.post(
		path =group_id + '/feed', 
		message = text,
		link = link_in
	)
	
def postImage(token_in, img_path):
	g = GraphAPI(token_in)
	g.post(
		path =group_id + '/photos', 
		source = open(img_path, 'rb'),
	)

def writeComment(page_token_in, comment, dest_id, link_in = ""):
	pg = GraphAPI(page_token_in)
	pg.post(
		path = dest_id + '/comments',
		message = comment,
		link = link_in
	)

# Print all messages from group feed.
def printAllMessage():
	graph = GraphAPI(api)
	x = graph.get(
		path = group_id + '/feed',
		page = False,
		retry = 3
	)
	f = open("comments.txt", "w")
	for i in range(len(x['data'])):
		if("message" in x['data'][i].keys()):
			f.write(x['data'][i]['message'])
			f.write('\n')
			print(x['data'][i]['message'])

def run_platform():
	startTime = time.time()
	# Repeat the process when t secs lapsed, where t is randomly chosen.
	# t = random.sample(duration, 1)[0]
	
	## for demo purposes, set t = 8.
	t = 8
	count = 1
	while True:
		try:
			p = random.sample(bots, 1)[0]
			m = random.sample(messages, 1)[0]
			postMessage(p, m)
			messages.remove(m)
			print(str(count) + " message(s) posted on feed.")
			if(count % 5 == 0): # comment much less often than posting
				randomComment()
				hitLike(random.sample(bots, 1), "363436647695274")
				print(str(count*0.5)[0] + " comment(s) posted.")
			count += 1
			time.sleep(t - ((time.time() - startTime) % t))
		except:
			print("Error posting message")
			exit(0)

def randomComment():
	p = random.sample(bots, 1)[0]
	c = random.sample(comments, 1)[0]
	post_id = "363436647695274"
	time.sleep(10) # avoid posting and commenting at the same time to make it more realistic.
	writeComment(p, c, post_id)

# Function that can like a comment
def hitLike(page_token_in, post_id_in):
	g = facebook.GraphAPI(page_token_in)
	post = g.get_object(post_id_in)
	g.put_like(post['id'])

# Brief Overview
# 1. Post a message
# 2. Post a message on feed with a link
# 3. Respond to somebody else's posts/comments
# 4. Like other people's posts

if __name__ == "__main__":
	# printAllMessage() 
	# postMessage(ewhites, "Hello, how's everyone doing today?")
	# postMessage(amaher, "Check this video out about a day at the University of Michigan, this is amazing!🤘", "https://www.youtube.com/watch?v=nlxp66eVDsY")
	# post_id = "363436647695274"
	# hitLike(ewhites, post_id)
	run_platform()

# TODO: NLP Respond to comments
# Tensor Flow -- https://github.com/deepmipt/DeepPavlov


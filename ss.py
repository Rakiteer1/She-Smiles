# -*- coding: utf-8 -*-

from sys import exit


def ask_4_return():
	"""I want this function to wait for a return."""
	# This is the carriage return in unicode I think. "\u21B5"
	raw_input(); #print "\r\r\r\r\r\r\r"
	
def ask_4_input():
	
	global next
	
	next = raw_input('> ')
	
def choice(number, string):
	
	global next
	
	if number in next:
		return True
	elif string in next:
		return True
	else:
		return False

def multiple_chosen():

	global next
	global cue
	options = 0
	
	for i in cue:
		options += 1
	
	tally = 0
	
	for i in range(options):
		temp = cue[i]
		for a in temp:
			if a in next:
				tally += 1
				break
				
	if tally > 1:
		return True
	else:
		return False
	
def printy(string):
	"""Requires a returm before executing the next line."""
	print string,
	ask_4_return()

def dead(why):
	print why, "Good job!"
	exit(0)

def prologue(): # status: working involves two choices.
	
	global next
	global cue
	
	printy("You're walking home on a path.")
	printy("To the left is forest, to the right a sheer cliffside.")
	printy("Up ahead the path veers sharply to the right.")
	printy("You Can't see around the corner of the cliffside.")
	printy(". . .")
	printy("You are closing in on the turn.")
	printy("The young buck is heavy across your shoulders.")
	printy("Not much longer.")
	printy("It's downhill to the town after.")
	printy("You turn around the corner when suddenly . . .")
	printy("A girl.")
	printy("You both manage to stop and prevent a horrible collision.")
	
	print "There is space to the right and to the left."
	print "1. Move to the right."
	print "2. Move to the left."
	print "3. Do nothing."
	
	cue = [
	['1','right','r'],
	['2','left','l'],
	['3','nothing'],
	]
	
	while True: # processes previously printed choices.
	
		ask_4_input()
		
		if multiple_chosen():
			print "I'm confused. What do you mean?"
			
		elif choice('1', 'right'):
			chosen = 'right'
			other = 'left'
			break
		
		elif choice('2', 'left'):
			chosen = 'left'
			other = 'right'
			break
			
		elif choice('3', 'nothing'):
			printy("The girl passes you. And leaves.")
			dead("You fail to progress the story.")
			
		else:
			print "I don't understand."
	
	
	printy("She also steps to the %s." % chosen)
	
	print "What do you do?"
	print "1. Step to the %s." % other
	print "2. Do nothing."
	
	cue = [
	['1','%s' % other],
	['2','nothing'],
	]
	
	while True: # processes previously printed choices.
	
		ask_4_input()
		
		if multiple_chosen():
			print "I don't understand. What do you mean?"
		
		elif choice('1', other):
			printy("She also steps to the %s." % other) 
			printy("She looks up at you.")
			printy("She smiles brightly and passes around you.")
			printy("You remain in place smitten.")
			printy("You continue on you're way pondering.")
			title_screen()
		
		elif choice('2', 'nothing'):
			printy("The girl passes you. And leaves.")
			dead("You fail to progress the story.")
		
		else:
			print "I don't understand."

def title_screen():
	printy(" . . .")
	printy(" . . .")
	printy(" . . .")
	print """
       .---. .-. .-.,---.      .---.         ,-.,-.    ,---.     .---.  . . .
      ( .-._)| | | || .-'     ( .-._)|\    /||(|| |    | .-'    ( .-._)      
     (_) \   | `-' || `-.    (_) \   |(\  / |(_)| |    | `-.   (_) \         
     _  \ \  | .-. || .-'    _  \ \  (_)\/  || || |    | .-'   _  \ \        
    ( `-'  ) | | |)||  `--. ( `-'  ) | \  / || || `--. |  `--.( `-'  )       
     `----'  /(  (_)/( __.'  `----'  | |\/| |`-'|( __.'/( __.' `----'          
            (__)   (__)              '-'  '-'   (_)   (__)
					
					
                               By Rakiteer1
	"""
	printy("Start?")
	embark()

def embark():
	print "This is the embark function."
	printy("You start your journey.")
	up_the_slope()

def up_the_slope():
	print "up_the_slope function has been called."
	printy("This is where you climb to the top of the mountain.")
	rock_giant()	

def rock_giant():
	print "rock_giant function has been called."
	printy("This is where you converse with the rock golem at the mountain and you're reassured.")
	cavernous_descent()

def cavernous_descent():
	print "cavernous_descent function has been called."
	printy("This is where you descend through the caves to the base of the mountain.")
	printy("At the end of this stage you learn you were wronged and you despair.")
	red_djinn()

def red_djinn():
	print "red_djinn function has been called."
	printy("Here you learn that your calamity could have been averted by someone you trust.")
	printy("Sadness is replaced by anger. And you lash out.")
	printy("You learn to mistrust people, and gain a great determination.")
	exit(0)

prologue()
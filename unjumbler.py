# Winson Li
# Software Engineering
# Assignment 1: Jumble
# unjumbler.py

from collections import Counter
import sys

with open('words.txt', 'r') as file: # word file contains list of english words for dictionary
    dictionary= file.read() # read file and makes it dictionary

# clears the dictionary of junk like spaces and hypens, makes sure it's lowercase
dictionary= [word.replace(" ","").replace("'","").replace("-","").lower() for word in dictionary.split('\n')]

#function that solves the jumble by finding the possible combinations of the letters in the jumble
def solve(jumble):
		letters_count= Counter(jumble) # get the letter count
		combinations= set()
		for word in dictionary: # loop
			file= 0
			if len(jumble) == len(word): # find and match each letter of the jumble to unjumble possibles
				if not (set(word) - set(jumble)):
					for letter, count in Counter(word).items():
						if count != letters_count[letter]:
							file = 1 
							break
					if not file:
						combinations.add(word)				
		if combinations:
			print("Here are the possible unjumbled word combinations: " , combinations) # outputs of the possible unjumbled words 
		else:
			print("Words not found.") # output if no words are found
			
if __name__ == '__main__':
	while(1):
		jumble= input("Please enter your jumble word: ").strip().lower().replace(" ","") # takes input jumbled word and makes lowercase
		solve(jumble)
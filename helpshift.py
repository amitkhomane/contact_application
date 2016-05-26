# I am not using any DB here to avoid any dependancy here. Application work and saves all the data for 1 run only.
# using python 2.7
# checked pep8 standard 'pep8 helpshift.py --max-line-length=120 --ignore=W191'

# instructions to run program.
# run command in terminal as, python helpshift.py and follow the instructions.


import sys
from difflib import SequenceMatcher

contacts = {}
LAST_ID = 0


def generate_id():
	'''
	Generates unique identifier for the contact
	'''
	global LAST_ID
	LAST_ID = LAST_ID + 1
	return LAST_ID


def add_contact():
	'''
	add new contact in contact list.
	'''
	name = read_input("Enter name: ")
	if len(name) > 50:
		print 'Name seems to be too long. Select choice again'
		return None
	id = generate_id()
	contacts[id] = {'name': name.strip()}
	print contacts


def search_contact():
	'''
	search for the key in contact. Show best matches first.
	'''
	key = read_input("Enter key to search: ")
	match = {}
	for id, cont in contacts.iteritems():
		score = similarity_score(cont['name'], key)
		if score > 0:
			match[score] = cont['name']
	print "---Matching contacts----\n"
	for k in sorted(match):
		print match[k]
	print "\n----------------------\n"


def read_input(msg):
	'''
	read user input
	- param 'msg': message to print
	- type 'msg': str

	- return 'input_value': value entered by user
	- type 'input_value': str
	'''
	input_value = raw_input(msg)
	return input_value


def switch_case(choice):
	'''
	execute function according to provided choice.

	- param 'choice': choice from the user
	- type 'choice': str
	'''
	if choice == '1':
		add_contact()
	elif choice == '2':
		search_contact()
	elif choice == '3':
		exit_contact()
	else:
		print "**************************************************"
		print "You have entered invalid choice. Please enter again"
		print "**************************************************\n"


def exit_contact():
	'''
	exit from the application.
	'''
	read_input("Bye press any key to exit")
	sys.exit(0)


def similarity_score(name, key):
	'''
	string matching score of the two provided string.

	ref. http://stackoverflow.com/questions/17388213/python-string-similarity-with-probability

	- param 'name': name from contact to match
	- type 'name': str

	- param 'key': search key to match to the name
	- type 'key': str

	- return : sequence matcher score
	- type : float
	'''
	score = 0
	if key in name:
		score = SequenceMatcher(None, name, key).ratio()
	return score

if __name__ == '__main__':
	'''
	Main function. Start of the script.
	'''
	user_choice = None
	while user_choice != 3:
		print "Well come to contact application\n"
		print "1. Add contact"
		print "2. Search contact"
		print "3. Exit"

		user_choice = read_input("Enter you choice: ")
		switch_case(user_choice)

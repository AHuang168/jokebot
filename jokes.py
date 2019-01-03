"""
CSM tech exercise
"""

import time, csv, sys, json, requests, os

def prompt_punchline(prompt, punchline):
	print(prompt)
	time.sleep(2)
	print(punchline, "\n")

def contin():
	print("Wanna continue? next / quit")
	user = input().replace(" ", "").lower()
	if user == "quit":
		print("kk\n")
		return False
	elif user == "next":
		return True
	print('das invalid\n')
	return contin()

#handle inputs from user before calling prompt_punchline from local csv
def main():
	if len(sys.argv) == 1:
		main2()
		exit()
	if not os.path.isfile(sys.argv[1]):
		print('\ncsv file doesn\'t exist\n')
		exit()
	with open(sys.argv[1]) as csvfile:
		line = csv.reader(csvfile, delimiter = ',')
		print('Do you want to hear the first joke? (yes / no)')
		user = input().replace(" ", "").lower()
		print()
		if user == 'yes':
			for seg in line:
				prompt_punchline(seg[0], seg[1])
				if not contin():
					break
				print()
			print("No more jokes!")
		elif user == 'no':
			print("aight")
		else:
			print("das invalid")
			main()

#from online

#joke 'title' answer 'selftext'
def main2():
	json = requests.get('https://www.reddit.com/r/dadjokes.json', headers = {'User-agent': 'bot'}).json()
	filtered = {}
	for key in json['data']['children']:
		if key['data']['over_18'] == False:
			first_word = key['data']['title'].split(' ')[0]
			if first_word == 'What' or first_word == 'Why' or first_word == 'How':
				filtered[key['data']['title']] = key['data']['selftext']
	print('Do you want to hear the first joke? (yes / no)')
	user = input().replace(" ", "").lower()
	print()
	if user == 'yes':
		for key, val in filtered.items():
			prompt_punchline(key, val)
			if not contin():
				break
			print()
		print("No more jokes!")
	elif user == 'no':
		print("aight")
	else:
		print("das invalid")
		main2()

main()


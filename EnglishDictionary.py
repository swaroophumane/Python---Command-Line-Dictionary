import json
from difflib import get_close_matches

with open('data.json'):
	data = json.load(open('data.json'))
	def translate(w):
		if w in data:
			return data[w]
		elif len(get_close_matches(w, data.keys())) > 0:
			yn = input(f"Did you mean '{get_close_matches(w, data.keys())[0]}' instead? Enter Y if yes, N if no. ")
			if yn == 'Y':
				return data[get_close_matches(w, data.keys())[0]]
			elif yn =='N':
				return "The Word Dosent Exist, Please Double Check It..!"
			else:
				return "We Didnt Understand Your Query"
		else:
			return 'The Word Dosent Exist, Please Double Check It..!'

	word = input("Enter Word: ").lower()

	output = translate(word)

	if type(output) == list:
		for item in output:
			print("- " + item)
	else:
		print(output)
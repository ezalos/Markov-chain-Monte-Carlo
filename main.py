import json

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "

def construct_dic(big=True):
	dic = {}
	for a in alphabet:
		dic[a] = construct_dic(False) if big else 0
	dic['0-9'] = construct_dic(False) if big else 0
	dic['!.?'] = construct_dic(False) if big else 0
	dic['UTF'] = construct_dic(False) if big else 0
	return dic

def isascii(c):
	return ord(c) < 128

def get_key(letter):
	if letter.isdigit():
		ret = '0-9'
	elif not isascii(letter):
		ret = 'UTF'
	elif letter.isalpha():
		ret = letter.upper()
	else:
		ret = '!.?'
	return ret

def backup(content, path):
	with open(path, 'w') as fout:
		json_dumps_str = json.dumps(content, indent=4)
		print(json_dumps_str, file=fout)

if __name__ == "__main__":
	mark = construct_dic()
	
	with open("fontaine.txt", "r") as f:
		corpus = f.read()

	for i in range(len(corpus) - 1):
		mark[get_key(corpus[i])][get_key(corpus[i + 1])] += 1

	print(mark)
	backup(mark, "markov.json")

listOfFile = ['train_tag.txt', 'valid_tag.txt']
for file in listOfFile:
	with open(file,'r+') as f:
		seq = 0
		for line in iter(f.readline, ''):
			seq+=1
			if line[-2] == ';':
				# print(seq)
				pos = f.tell()
				f.seek(pos - 2)
				f.write(' ')
				f.seek(pos)

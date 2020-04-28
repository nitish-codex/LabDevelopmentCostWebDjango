geneID = open('IDgene.txt', 'r')
geneDiseaselist = open('geneDiseaselist.txt', 'r')
newGDL = open('new_geneDiseaselist.txt', 'a+')
DICT = {}
for line in geneID:
	ids = line.strip().split('\t')[0]
	gene = line.strip().split('\t')[1]
	if ids in DICT:
		value = DICT[ids]
		value.append(gene)
		DICT[ids] = value
	else:
		value = []
		value.append(gene)
		#print(value)
		DICT[ids] = value
'''
for key, value in DICT.items():
	print(key)
	print(value)
'''
for i in geneDiseaselist:
	key = i.strip().split('\t')[0]
	D = i.strip().split('\t')[1]
	print(key, DICT[key])
	genelist = DICT[key]
	genelist = ' '.join(genelist)
	row = key+'\t'+D+'\t'+genelist+'\n'
	newGDL.write(row)

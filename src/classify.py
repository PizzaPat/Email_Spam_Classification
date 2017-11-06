#import pandas as pd
from collections import Counter
import re
print("Start processing")

words = list()
wordsSpam = list()
wordsHam = list()
lineNum = 0;

with open('../spam_train.txt') as f:
	for line in f:
		if lineNum < 4000:
			print(line)
			tmpList = line.lower()
			tmpList = re.sub('[^a-z\ \']+', " ", tmpList)
			tmpList = list(tmpList.split())
			tmpList = list(set(tmpList))
			words =  tmpList + words
			lineNum = lineNum + 1

			if line[0] == '0':
				wordsHam = tmpList + wordsHam
			elif line[0] == '1':
				wordsSpam = tmpList + wordsSpam
			else:
				pass

''' count all the words that exist in the list and then
	transform them into list once again '''
d = dict(Counter(words))
d2 = dict(Counter(wordsHam))
d3 = dict(Counter(wordsSpam))


print('///// Test case for keyword \'aniwai\'')

print('--------------------------Total from 4000------------')
for key, value in d.items():
	if value >= 1 and key == 'anywai':
		print('Keyword:', key, ' Value:', value)
		keyHamSpam = key
		valueHamSpam = value

print('--------------------------Words Ham------------------')

for key, value in d2.items():
	if value >= 1 and key == 'anywai':
		print('Keyword:', key, ' Value:', value)
		keyHam = key
		valueHam = value

print('--------------------------Words Spam-----------------')

for key, value in d3.items():
	if value >= 1 and key == 'anywai':
		print('Keyword:', key, ' Value:', value)
		keySpam = key
		valueSpam = value


print('-----------Probability of Ham of \'anywai\' is-------------')

print('---------Ham------------')
print('computation: ',valueHam,'/',valueHamSpam)
print('---------Spam-----------')
print('computation: ',valueSpam,'/',valueHamSpam)
print('\n\n\n\n')
result = valueHam /valueHamSpam
print('P(Ham)=', result)
result = valueSpam /valueHamSpam
print('P(Spam)=', result)


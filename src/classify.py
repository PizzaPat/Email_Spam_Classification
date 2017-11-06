#import pandas as pd
from collections import Counter
import re
print("Start processing")

counts = list()
i=0

words = list()
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

'''
with open('../spam_test.txt') as fp:
	for i, line in enumerate(fp):
		if i < 4000:
			line = fp.readlines()
			print(line)
			tmpList = line.lower()
			tmpList = re.sub('[^a-z\ \']+', " ", tmpList)
			words = list(tmpList.split()) + words
fp.close()
'''

d = dict(Counter(words))

print('------------Done------------')
for key, value in d.items():
	if value >= 30:
		print('Keyword:', key, ' Value:', value)


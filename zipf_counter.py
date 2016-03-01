#!/usr/bin/env python3
import sys
import os
import re
import struct
import time

import matplotlib.pyplot as plt

from collections import Counter

from nltk.tokenize import RegexpTokenizer

if len(sys.argv) < 2:
	print("zipf_counter.py <txt-files-dir>")
	exit()

files_dir = sys.argv[1]
print("Scanning directory...")
tokenizer = RegexpTokenizer(r'\w+')		
start_time = time.time()
file_count = 0
sentence_splitter = re.compile(r' *[\.\?!][\'"\)\]]* *')
total_count = Counter()
for file in os.listdir(files_dir):
	if file.endswith(".txt"):
		start_time_file = time.time()
		with open(files_dir+"/"+file, encoding="latin_1") as f:
			text = f.read()
			text = text.lower()
			text = re.sub('<[^<]+?>', ' ', text)
			words = list(tokenizer.tokenize(text))
			tokens = Counter(words)
			total_count += tokens
		end_time_file = time.time()
		file_count += 1
		print("File %d: %s in %0.4f seconds" % (file_count, file, end_time_file - start_time_file))
		#print(total_count)
	#break
end_time = time.time()
#for key, value in db:
#	print('KEY=%s VALUE=%s' % (key.decode('utf-8'), struct.unpack('I', value)[0]))

print("TOTAL: words: %d in %0.4f seconds" % (len(total_count), end_time - start_time))

sorted_total = total_count.most_common()
print(sorted_total[:20])


plt.plot(list(range(1,len(sorted_total)+1)), [x[1] for x in sorted_total])
plt.title("Zipf's Law")
plt.axis([1, len(sorted_total)+1, 1, sorted_total[0][1]])
plt.ylabel('Frequência')
plt.yscale('log')
plt.xlabel('Rank')
plt.xscale('log')
plt.show()

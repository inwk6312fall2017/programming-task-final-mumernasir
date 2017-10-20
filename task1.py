
fin=open("Book1.txt")
fin1=open("Book2.txt")
fin2=open("Book3.txt")
def long_word(fin):
	largestWord=""
	largestLen=0
	for line in fin:
		line=line.split()
#	print(line)
		for word in line:
			if len(largestWord)<len(word):
	       			largestWord=len(word)
        			largestWord=word
	
	return largestWord


word1=long_word(fin)
word2=long_word(fin1)
word3=long_word(fin2)

word4=[word1,word2,word3]
#print(word4)
largestWords=""
largestLens=0
for words in word4:
    if len(largestWords)<len(words):
            largestWords=len(words)
            largestWords=words
print ("The largest word in all 3 books is ",largestWords)




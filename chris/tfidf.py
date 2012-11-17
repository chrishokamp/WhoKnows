#!/usr/bin/python

#tfidf module which takes two vectors and returns cosine similarity
from math import log, sqrt



#TODO: not implemented!!
#This code uses Ravi's parsing module
#def buildQueryVector(query): 
	

#first build the idf dictionary
def buildIndexes(dictMatrix):

	#this returns a dictionary of 
	#remember that we'll need the global doc count	
	globalDocCount = len(dictMatrix.keys())
        idfIndex = {} 
	tfIndex = {}	

	for person in dictMatrix.keys():
		singleDocHash = {}
		for word in dictMatrix[person]:
			currentVal = singleDocHash.get(word, 0)
			singleDocHash[word] = currentVal + 1		
		#add the doc vector to the tf matrix
		tfIndex[person] = singleDocHash	        

		#+1 for each key in the doc
		for key in singleDocHash.keys():
			print 'key: ' + str(key)
			currentVal = idfIndex.get(key, 0)
			print 'currentVal is: ' + str(currentVal)
			currentVal += 1
			print 'currentVal is: ' + str(currentVal)
			idfIndex[key] = currentVal 

	#calulate the final idf values 	
	for word in idfIndex.keys():
		rawVal = idfIndex[word]
		print 'word: ' +str(word) + ' rawVal: ' + str(rawVal)	
		print 'globalDoc: ' + str(globalDocCount)
		finalVal = log(globalDocCount/rawVal) + 1		
		idfIndex[word] = finalVal

	return (idfIndex, tfIndex)


def tfidfIndex(idfIndex, tfIndex):

	tfidfIndex = {} 
	for person in tfIndex.keys():
		personHash = {}
		for word in tfIndex[person].keys():
			if (word in idfIndex):
				idfVal = idfIndex[word]
				#TODO: fix errors here
				tfVal = tfIndex[person][word]
				tfidfVal = idfVal * tfVal  						
				personHash[word] = tfidfVal
		tfidfIndex[person] = personHash

	return tfidfIndex	
		




#COSINE SIMILARITY
def cosineSim(vec1, vec2): 
	
	def dotProduct (vector1, vector2):
		#vectors are dictionaries
		#iterate over vector and see if the words exist, if they do, dot product 
		dotProduct = 0
		for word in vector1.keys():
			if (word in vector2):
				dotProduct += vector1[word] * vector2[word]				
		return dotProduct

	def eucLen(vector):
		total = 0
		for value in vector.keys():
			total += vector(value)

		return sqrt(total)

	cosSim = dotProduct(vec1, vec2)/(eucLen(vec1) * eucLen(vec2))

	return cosSim 






 


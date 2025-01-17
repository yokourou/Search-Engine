from itertools import chain
from collections import defaultdict
import numpy
import pickle
import sys
import copy

with open("tfidf.dict",'rb') as f:
	tfidf = pickle.load(f)
	
with open("tokInfo.dict",'rb') as f:
	tokInfo = pickle.load(f)

with open("pageRank.dict",'rb') as f:
	pageRankDict = pickle.load(f)

print("Normalizing tf idf...",end="")
tfidfNorm = copy.deepcopy(tfidf)
for doc, tokens in tfidfNorm.items():
    norm_factor = numpy.linalg.norm(list(tokens.values()))
    if norm_factor > 0:
        tfidfNorm[doc] = {token: tfidfNorm[doc][token] / norm_factor for token in tokens}
    else:
        tfidfNorm[doc] = tokens
print("done.")



# Returns the topN documents by token relevance (vector model)
def getBestResults(queryStr, topN, tfidfMatrix):
	query = queryStr.split(" ")
	res = defaultdict(float)
	for doc, tokens in tfidfMatrix.items():
		score = 0.0
		for token in query:
			if token in tokens:
				score += tokens[token]
			if score > 0:
				res[doc] = score
	best_results = sorted(res.items(), key=lambda x: x[1], reverse=True)[:topN] 
	return [doc for doc, score in best_results]

# Sorts a list of results according to their pageRank
def rankResults(results):
	return sorted(results, key=lambda x: pageRankDict.get(x, 0), reverse=True)


def printResults(rankedResults):
	for idx,page in enumerate(rankedResults):
		print(str(idx+1) + ". " + page)



query = "darwin" # or sys.argv[1]
top = 15			 # number of results to show

print("Results for ",query,"\n===========")
results = getBestResults(query,top,tfidf)
printResults(results)

print("\n\nResults after normalization for ",query,"\n===========")
results = getBestResults(query,top,tfidfNorm)
printResults(results)


print("\n\nResults after ranking for ",query,"\n===========")
 #TO COMPLETE
 #TO COMPLETE
query = queryStr.split(" ")
	res = defaultdict(float)
	for doc, tokens in tfidfMatrix.items():
		score = 0.0
		for token in query:
			if token in tokens:
				score += tokens[token]
			if score > 0:
				res[doc] = score
	best_results = sorted(res.items(), key=sortByScore, reverse=True)[:topN] 
	return [doc for doc, score in best_results]
# bestPageSimilarity = list(reversed([ searchRes[i] for i in numpy.argsort(searchRes)[-10:] ]))
# print(bestPageSimilarity)



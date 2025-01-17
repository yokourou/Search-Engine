import sys
import xml.etree.ElementTree
from collections import defaultdict
import numpy
import re
import pickle
import glob
from itertools import chain
from collections import Counter
import math

xmlFiles = list(chain(*[ glob.glob(globName)  for globName in sys.argv[1:] ]))
print("Files as input:", xmlFiles)

docs = dict()

##############################
print("Parsing XML...")
##############################
for xmlFile in xmlFiles:
	pages = xml.etree.ElementTree.parse(xmlFile).getroot()

	for page in pages.findall("{http://www.mediawiki.org/xml/export-0.11/}page"):
		titles = page.findall("{http://www.mediawiki.org/xml/export-0.11/}title")
		revisions = page.findall("{http://www.mediawiki.org/xml/export-0.11/}revision")
	
		if titles and revisions:
			revision = revisions[0] # last revision
			contents = revision.findall("{http://www.mediawiki.org/xml/export-0.11/}text")
			if contents:
				docs[titles[0].text] = contents[0].text 



# Some regEx for parsing
cleanExtLinks = r"\*?\s*'{0,2}\[http[^\]]+\]\s*[^\n]*'{0,2}"# * ''[]'' ou *[] * []    
linkRe = r"\[\[[^\]]+\|([^\|\]]+)\]\]|\[\[([^\|\]]+)\]\]"
removeLinkRe = r"\[\[[^\]]+\|([^\|\]]+)\]\]"  # Lien de format [[lien | texte]]
removeLink2Re = r"\[\[([^\|\]]+)\]\]"  # Lien simple [[lien]]
wordRe = "[a-zA-Z\-]+"  # Mot composé de lettres et tirets
stopWords = ["-"]




print("Extracting links, transforming links in text, tokenizing, and filling a tok-doc matrix...")
links = dict()
doctok = dict()
for idx,doc in enumerate(docs):
	if idx%(len(docs)//20) == 0:
	  	print("Progress " + str(int(idx*100/len(docs)))  +"%")
	links[doc] = list()	
	for link in re.finditer(linkRe,docs[doc]):
		if link.group(1):
			target = link.group(1).split('|')[0]
			if target in docs.keys():
				#print(doc + " --> " + target)
				links[doc] += [target]
			
	cleanDoc = re.sub(cleanExtLinks,"",docs[doc])
	# transform links to text
	docs[doc] = re.sub(removeLinkRe,r"\1",cleanDoc)
	docs[doc] = re.sub(removeLink2Re,r"\1",docs[doc])	
	# fill the doctok matrix
	doctok[doc] = list()
	for wordre in re.finditer(wordRe,cleanDoc):
		word = wordre.group(0).lower()
		if word not in stopWords:
			doctok[doc] += [word]

print("done.")

print("Building tf-idf table...")
docList = doctok.keys()
Ndocs = len(docList)


tokInfo = defaultdict(float) # tokInfo[tok] contains the information in bits of the token
tf = dict() # tf[doc][tok] contains the frequency of the token tok in document doc

###########################constructing the information of a token dict############################
# calculate number of docs including token t : 
for doc in docList:
	tokens_in_doc = doctok[doc]
	token_inter = [] 
	for token in tokens_in_doc : 
		if token in token_inter:
			pass
		else :
			token_inter.append(token)
			if token in tokInfo.keys():
				tokInfo[token] +=1.0 / Ndocs
			else :
				tokInfo[token] =1.0 / Ndocs
#calculate I(t) : nformation(tokent) = − log( nombre(doc including token t)/nombre(#docs )) 
for key in tokInfo.keys():
	tokInfo[key]  = - math.log(tokInfo[key])

###########################calculating the frequency matrix####### ############################# 
def nombre_occurence(l):
    # compte le nombre d'occurrences de chaque élément
    counts = Counter(l)
    return counts

for doc in docList : 
	tokens_in_doc = doctok[doc]
	counts = nombre_occurence(tokens_in_doc)
	tf[doc] = counts 

print("done.")
#  TF-IDF = (nombre(token in D)/nombre( tokens in D)) × I(token)
print("creating tf-idf...",end="")
tfidf = defaultdict(dict) # this should be in reverse sparse format
for doc in docList : 
	tokens_in_doc = doctok[doc]
	nombre_tokens = len(tokens_in_doc)
	for token in tokens_in_doc :
		tfidf[token] = (tf[doc][token]/nombre_tokens)*tokInfo[token]    
print("done.")



print("Saving the links and the tfidf as pickle objects...")
with open("links.dict",'wb') as fileout:
	pickle.dump(links, fileout, protocol=pickle.HIGHEST_PROTOCOL)

with open("tfidf.dict",'wb') as fileout:
	pickle.dump(tfidf, fileout, protocol=pickle.HIGHEST_PROTOCOL)

with open("tokInfo.dict",'wb') as fileout:
	pickle.dump(tokInfo, fileout, protocol=pickle.HIGHEST_PROTOCOL)

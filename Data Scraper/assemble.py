import random
import re
from ekphrasis.classes.segmenter import Segmenter
listOfFILEcomments = []
listOfFILEposts	   = []
listOfFILEtags	   = []
# for i in range(0,17):
# 	listOfFILEcomments.append('allcomments' + str(i) + '.txt')
# 	listOfFILEposts.append('allposts' + str(i) + '.txt')
# 	listOfFILEtags.append('alltags' + str(i) + '.txt')

seg_eng = Segmenter(corpus="english")

listOfFILEcomments = ['allcomments.txt']
listOfFILEposts = ['allposts.txt']
listOfFILEtags = ['alltags.txt']

fhc = open('finalallcomments.txt','a+')
fhp = open('finalallposts.txt','a+')
fht = open('finalalltags.txt','a+')
for commentFILE,postFILE,tagFILE  in zip(listOfFILEcomments,listOfFILEposts,listOfFILEtags):
	commentGenerator = open(commentFILE, 'r')
	postGenerator = open(postFILE, 'r')
	tagGenerator  = open(tagFILE, 'r')
	for comment,post,tag in zip(commentGenerator,postGenerator,tagGenerator):
		if comment.strip() and post.strip() and tag.strip():	
			fhc.write(comment)
			fhp.write(post)
			fht.write(';'.join([seg_eng.segment(w) for w in tag.split(';') if w]))
	commentGenerator.close()
	postGenerator.close()
	tagGenerator.close()

fhc = open('finalallcomments.txt','r')
fhp = open('finalallposts.txt','r')
fht = open('finalalltags.txt','r')

data = [ (random.random(),line1,line2,line3) for line1,line2,line3 in zip(fhc, fhp, fht) ]

fhc.close()
fhp.close()
fht.close()

fhRanComments = open('randomComments.txt','a+')
fhRanPosts = open('randomPosts.txt','a+')
fhRanTags = open('randomTag.txt','a+')

data.sort()

for _, line1,line2,line3 in data:
	fhRanComments.write(line1)
	fhRanPosts.write(line2)
	fhRanTags.write(line3)

fhRanComments.close()
fhRanPosts.close()
fhRanTags.close()


	
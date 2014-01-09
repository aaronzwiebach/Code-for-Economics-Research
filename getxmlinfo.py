import sys
sys.path.append('/usr/lib/python2.6/site-packages/')
sys.path.append('/usr/lib/python2.4/site-packages/')
from BeautifulSoup import BeautifulSoup
import nltk
import sys
import re
import os
from os import listdir
from os.path import isfile, join
import csv
import re
import itertools

#Method parses through xml file extracts and writes: id, timestamp, user, userid, size, to a specified outfile.
def writexmllinescript(outfile1, xmlsoup):
	revisiontags= xmlsoup.findAll('revision')
	print xmlsoup
	for revision in revisiontags:
		
		id1= str(revision.id.contents)
		id2=id1.strip("[u")
		id3= id2.strip("]")
		id4= id3.strip("\'")
		

		timestamp1= str(revision.timestamp.contents)
		timestamp2= timestamp1.strip("[u")
		timestamp3= timestamp2.strip("]")
		timestamp= timestamp3.strip("\'")
		
		user1= str(revision.user.contents)
		user2= user1.strip("[u")
		user3= user2.strip("]")
		user =user3.strip("\'")	
		
		userid1= str(revision.userid.contents)
		userid2= userid1.strip("[u")
		userid3=userid2.strip("]")
		userid= userid3.strip("\'")
		
		size1= str(revision.size.contents)
		size2= size1.strip("[u")
		size3= size2.strip("]")
		size= size3.strip("\'")
		
		outline= id4+ "\t" + timestamp+ "\t" +user+ "\t" +userid+ "\t" +size+ "\n"
		
		outfile1.write(outline)

def writexmlinfocsv(person, outfile, xmlsoup):
        writexmllinescript(outfile, xmlsoup)


							     
										

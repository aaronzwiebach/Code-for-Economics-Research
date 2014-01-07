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

#Method gets individuals unique Wiki-Name
def getnewwpmethod(soup):
	#Find all 'script' tags
	result= str(soup.findAll('script'))
	#string method to isolate the unqiue name that is alwasys found between the two arguements
	newresult=str(result[result.find("wgPageName")+1:result.find("wgTitle")])
	newerresult = str(newresult.strip("gPageName"))
	head, sep, tail = newerresult.partition(":")
	newstring = tail[:-3]
	finalstring= newstring[:-0]
	return newstring 


#Gets files from lists of wiki htmls identical to rawdata   
def getfiles(foldername):

	infile = "filelist.txt"
	infileh = open(infile, "r")
	onlyfiles = []
	for line in infileh:
		onlyfiles.append(line.strip())

	return onlyfiles

#Using nltk-get number of characters in the body of the wiki text
def getcharsizeinfo(soup):
	#Find all 'div' tags with 'id' attribute: content_wrapper
	result= str(soup.findAll('div',{'id':'content_wrapper'}))#the body of the html page

        clean_text = nltk.clean_html(result)
	return len(clean_text)

#Method extracts date of revision written in plain text
def getlastrevdate(soup):
	result= str(soup.findAll('a',{'id':'mw-mf-last-modified'}))#Find all <a> tags with attribute:'id':'mw-mf-last-modified'
	newresult=result[result.find(">")+1:result.find("</a>")]
	newerresult= newresult.strip("Last modified on ")
	head, sep, tail = newerresult.partition(",")
	return head
#Method extracts time stamp of revision	
def gettimestamp(soup):
	stamps=soup.findAll('a',{'id':'mw-mf-last-modified'})#Find all <a> tags with attribute:'id':'mw-mf-last-modified'    
	for stamp in stamps:
		return stamp['data-timestamp']


#Method returns number of pictures on the page with width>75pxls
def getimginfo(soup, ):

    bigpix=[]
    images=soup.findAll("img", width=True)# Find all image tags with attribute width
    


    for img in images:
	    if int(img['width'])>75:
		    bigpix.append(img)


    return len(bigpix)

#Method calls each of the previous methods and outputs to a given outfile csv: unique wikiname, filenumber, #chars, #img, and a time stamp if there is one
def writelinescript1(filename, outfile, soup):

	 
	newwpname= str(getnewwpmethod(soup))
	finalwpname= newwpname.strip("\"")
	charsize = str(getcharsizeinfo(soup))
	imgNum= str(getimginfo(soup))
	timestamp =str(gettimestamp(soup))
	filename = str(filename.strip(".html"))
	lastrevdate= str(getlastrevdate(soup))
	outline =finalwpname+ "\t" +filename+ "\t" + charsize+ "\t" + imgNum+ "\t" + timestamp+ "\n"
	outfile.write(outline)
	
	
def writegeneralinfocsv(person, revisionfile, outfile, soup):
	writelinescript1(revisionfile, outfile, soup)
	

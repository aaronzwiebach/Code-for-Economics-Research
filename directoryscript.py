import sys
sys.path.append('/usr/lib/python2.6/site-packages/')
sys.path.append('/usr/lib/python2.4/site-packages/')
from BeautifulSoup import BeautifulSoup
import sys
import re
import os
from os import listdir
from os.path import isfile, join
import csv
import re
import itertools

#Import all other scripts.
from finalgetgeneralinfo import getnewwpmethod, getcharsizeinfo, getlastrevdate, gettimestamp, getimginfo, writelinescript1, writegeneralinfocsv
from finalgetimginfo import getlivepixinfo, getdeadpixinfo, writelinescript2, writeimginfocsv
from finalgetxmlinfo import *


root = "/mnt/nfs6/wikipedia.proj/rawdata/wikidata/"


playernum = int(sys.argv[1])
playerlist = open(root + "playerlist.txt","r")
lines=playerlist.readlines()
persons = [lines[playernum].strip()]


#For each person in playerlist...
for person in persons[:1]:
    
    #create Soup object out of their XML file
    xmlfilepath= root+person+"/"+person+".xml"
    xmlfilehandle= open(xmlfilepath, "r")
    xmlsoup= BeautifulSoup(xmlfilehandle)

    #Make a list containing all their revision files.
    path = root + person + "/revisions/"
    personsrevisionfiles= os.listdir(path)

    # Create Header line for individuals Img Info CSV
    personalgetimginfo=root+person+"/csvfiles/"+person+"imginfo.csv"
    outfile2= open(personalgetimginfo, "w")
    outline2= "revid\timg-name\twidth\tstatus\n"
    outfile2.write(outline2)
    
    #Create Header line for individuals General Info CSV
    geninfo=root+person+"/csvfiles/"+person+"generalinfo.csv"
    outfile1= open(geninfo, "w")
    outline1= "wpname\tfile-number\tcharsize\timgNum\ttimestamp\tlastrevdate\n"
    outfile1.write(outline1)
    
    #Create Header line for XML info csv
    getxmlinfo=root+person+"/csvfiles/"+person+"xml.csv"
    outfile3= open(getxmlinfo, "w")
    outline3= "id\ttimestamp\tuser\tuserid\tsize\n"
    outfile3.write(outline3)

    #And write the individuals xml info
    writexmlinfocsv(person,outfile3, xmlsoup)
     
                             
                            


    #For each revision file in the persons list of revisions
    for revisionfile in personsrevisionfiles:
        #Create a Soup object of that individual file
        filepath = root+person+"/revisions/"+revisionfile
        filehandle= open(filepath, "r")
        soup = BeautifulSoup(filehandle)
        


        #Write to their generalinfo csv and imginfo csv
        writegeneralinfocsv(person, revisionfile, outfile1, soup)
        writeimginfocsv(person, revisionfile, outfile2, soup)
        


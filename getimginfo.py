#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sys
sys.path.append('/usr/lib/python2.6/site-packages/')
sys.path.append('/usr/lib/python2.4/site-packages/')
from BeautifulSoup import BeautifulSoup
#import nltk
import sys
import re
import os
from os import listdir
from os.path import isfile, join
import csv
import re
import itertools


"""Gets files from lists of wiki htmls identical to rawdata"""
def getfiles(foldername):
    infile = "filelist.txt"
    infileh= open(infile, "r")
    onlyfiles= []
    for line in infileh:
        onlyfiles.append(line.strip())

    return onlyfiles

"""Method returns list of tuples, with info about 'live pictures'(pictures that actually appear on the wiki page): (pic name, width, status)"""
def getlivepixinfo(soup, ):
    images= soup.findAll("img", width=True) #find all <img> tags with parameter 'Width'
    tuplelist=[]
    for img in images:
        if int(img['width'])>50: #img must have width>75 pxls
            try: #If the img has an href tag as a parent then append tuplelist: (imgname, width)
                tuple= (img.parent['href'].strip("/wiki/File:"),img['width'])
                tuplelist.append(tuple)
            except KeyError: #If its parent isnt 'href' then append tuplelist: (img src, width)
                tuple= (img['src'], img['width'])
                tuplelist.append(tuple)
                
                
                
    return tuplelist

"""Method returns list of tuples, with info about 'dead pictures'(pictures that once appeared but no longer do): (pic name, width, status)"""
def getdeadpixinfo(soup):

    tags= soup.findAll(title=re.compile('.*File:.*'))#RE to find all 'title' attributes= 'File:'
    tuplelist2=[]
    for tag in tags:
    
        if tag.parent!= 'div': #if parent tag not equal to <div> set width equal to zero
        
            tuple2= (tag['title'].strip("File:"),0)
            tuplelist2.append(tuple2)
        else: #if parent tag equal to <div>
            divtag = tag.findParent('div')
            imgwidth = divtag['style']# i.e. the attribute that contains the width
            imgwidth = imgwidth.strip("width")
            imgwidth = imgwidth.strip("px;")
            tuple2= (tag['title'].strip("File:"), imgwidth)
            tuplelist2.append(tuple2)
    
    return tuplelist2

"""method for writing all the  information extracted about live/dead pix for a given wiki to a csv"""  
def writelinescript2(revisionfile, outfile, soup):


    revisionid = str(revisionfile.strip(".html")) #revision-ids            

    # LIVE IMAGES
    status = "live"
    livepix= getlivepixinfo(soup)#list of tuples with the specs from the live pix    

    if len(livepix)==0:#if there are no live images on given wikipedia html return none, except for revision-id
        jpgname = "None"
        width = "None"
        outline = revisionid + "\t" +jpgname+  "\t"  +width+  "\t"  +status +  "\n"
        outfile.write(outline)
        
        
    #if there are, extract  width and name
    else:
        for i in livepix:
            width = str(i[1])
            jpgname=str(i[0])
            outline = revisionid + "\t" +jpgname+  "\t"  +width+  "\t"  +status +  "\n"
            outfile.write(outline)
            
            
            
    # DEAD IMAGES
    status = "dead"
    deadpix= getdeadpixinfo(soup)#list of tuples with the specs from the dead pix    
    
    if len(deadpix)==0:#if there are no live images on given wikipedia html return none, except for rev-id
        jpgname = "None"
        width = "None"
        outline = revisionid + "\t" +jpgname+  "\t"  +width+  "\t"  +status +  "\n"
        outfile.write(outline)
        

    #if there are, extract  width and name 
    else:
        for i in deadpix:
            width = str(i[1])
            jpgname=str(i[0])
            outline = revisionid + "\t" +jpgname+  "\t"  +width+  "\t"  +status +  "\n"
            outfile.write(outline)
            

"""Method call the pervious writing method, to get specs from dead and live pics"""
def writeimginfocsv(person, revisionfile, outfile, soup):
    writelinescript2(revisionfile, outfile ,soup)
    






                                                    

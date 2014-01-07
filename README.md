Code-for-Economics-Research
===========================

Code written over summer 2013 for Abhishek Nagaraj at M.I.T. Sloan

GUIDE:
The following is an overview of the scripts written for the Wikipedia Project, it reviews the purpose of each script, in addition it acts as a reference on where to find relevant information.

The Scripts:
The main scripts for the Wikipedia Project are:

- finaldirectoryscript.py	   (master script)
- finalgetgeneralinfo.py	   revid -> (name, numchar, numimg, rev, timestamp)
- finalgetimginfo.py		   revid -> (imgname, img-width, dead/alive)
- finalgetxmlinfo.py		   revid -> (timestamp, username, userid, size)
- gettrafficinfo.py		

The above scripts can all be found in /mnt/nfs6/wikipedia.proj/odesk/finalscripts.

All scripts with the exclusion of gettrafficinfo.py are parsing scripts that extract information from the archives of WIkipedia articles written about famous people who are no longer alive. The revisions can be found in /mnt/nfs6/wikipedia.proj/rawdata/wikidata (a directory where each subdirectory is the name of a famous deceased person.) The archived revisions made to each persons Wikipedia article can be found in /mnt/nfs6/wikipedia.proj/rawdata/wikidata/famous_persons/revisions/:

finalgetgeneralinfo.py- extracts: 1) Number of characters per page 2) Number of images per page 3)Revision timestamp (If available)
finalgetimginfo.py- extracts: 1) The title of every image 2) The width of every image 3) The status of said image (whether it is a dead pictur or a live picture (i.e- does the picture still show up when you load the page.)
finalgetxmlinfo.py- extracts 1) Revision ID 2) Timestamp of the revisions 3)User Name 4)User ID 5) Size

finaldirectoryscript- Does not extract anything. The aforementioned scripts have all been formatted as methods and final directory script loops through each player in Wikidata and then loops through each of their Revisions and then calls the previous three scripts. After each loop finaldirectoryscript.py writes the information to three seperate CSV files that correspond to the three scripts. These files can be found at:
1)  /mnt/nfs6/wikipedia.proj/rawdata/wikidata/famous_persons/csvfiles/famous_persongeneralinfo.csv
2) /mnt/nfs6/wikipedia.proj/rawdata/wikidata/famous_persons/csvfiles/famous_personimginfo.csv
3) /mnt/nfs6/wikipedia.proj/rawdata/wikidata/famous_persons/csvfiles/famous_personxml.csv


gettrafficinfo.py- does not parse information, rather it grabs traffic info (from http://stats.grok.se/json)  for any given month in a given year for each specific famous_person and saves it to their directory as a JSON file. The files can be found at /mnt/nfs6/wikipedia.proj/rawdata/wikidata/famous_persons/Jsonfiles/famous_person_year_month.json.

Note: each script has been commented, for further infomation as to how the script runs and a more detailed look at its methods please visit the scripts themselves.



A caveat: As it stands there are 643 famous_persons in the /wikidata directory. Thus making the run time of any script very long, and more so exaggerated when many are run in succession. For this reason we have utilized Sloan's Equity server and SGE. In /finalscripts there exist two files script.sh and trafficscript.sh, script.sh runs finaldirectoryscript.py in parallel for many famous_persons at once and trafficscript.sh runs gettrafficinfo.py in parallel for many famous_persons at once. Both of these scripts dramatically decrease run time.


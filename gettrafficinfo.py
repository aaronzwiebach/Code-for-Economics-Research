import sys
import os
import urllib2
"""Method reads Json file for given month on a given year and writes it to famous_person's collection of /Jsonfiles"""
def getfile(playername, month, year):

    filename = "/mnt/nfs6/wikipedia.proj/rawdata/wikidata/"+str(playername)+"/Jsonfiles/"+ str(playername)+"_"+str(year)+str(month)+".json"
    filehandle= open(filename, "w")
    query = "http://stats.grok.se/json/en/" +str(year)+ str(month)+"/"+playername

    print "downloading file with URL LIB2"
    page= urllib2.urlopen(query)
    json= page.read()
    

    with open (filename, "wb") as code:
        code.write(json)
                
months = [1,2,3,4,5,6,7,8,9]
root = "/mnt/nfs6/wikipedia.proj/rawdata/wikidata/"


#In order to run this script on the grid utilize the following:

playernum = int(sys.argv[1])
playerlist = open(root + "playerlist.txt","r")
lines=playerlist.readlines()
playerlist = [lines[playernum].strip()]


"""Method loops through all the "players" in our database and runs get file on them"""
def extractjson(playerlist):
    for person in playerlist:#Loop through each player
        for month in range(1,9):#Through each month
            if month in months:#For single digit months add a zero, as is needed for the proper URL
                newmonth= "0"+str(month)
            else:
                newmonth= month
            for year in range(2008, 2013):#Loop through each year
                getfile(person, month, year)#Implement getfile
                print "Just finished writing "+person+"s info for" +str(12)+ " and " +str(2007)

#Run ExtractJson on our specified list of players
extractjson(playerlist)

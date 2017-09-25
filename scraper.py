"""
Shitpost Haiku Generator 0.1

"""
import json
import time
import re

from random import randint
from urllib2 import urlopen

#Traditional haiku consist of 17 on (also known as morae though often loosely translated as "syllables"), 
#in three phrases of 5, 7, and 5 on, respectively.[3]
#An alternative form of haiku consists of 11 on in three phrases of 3, 5, and 3 on, respectively.

board = "g"
words = []

try:
    url = "https://a.4cdn.org/" + board + "/catalog.json"
    site = urlopen(url)
    site = site.read()
except IOError:
    # open file
    print "you done goofed"

thestuff = json.loads(site)

threadIDs = []

for thread in thestuff[0]["threads"]:
    if thread["replies"] > 100:
        threadIDs.append(thread["no"])

id = randint(0, len(threadIDs)-1)

threadURL = ("https://a.4cdn.org/%s/thread/%d.json" % (board, threadIDs[id]))
threadcontent = urlopen(threadURL).read()
threadcontent = json.loads(threadcontent)

for reply in threadcontent["posts"]:
    try:
        try:
            threadwords = re.findall("(?<=[>.:;, ])([A-Za-z]{2,})(?=[.:;, ])", reply["com"])
            words = words + threadwords
        except UnicodeEncodeError:
            print "CRAP"
    except KeyError:
        print "SHIT"


    


# sys.flush




#words = ["hello"]
buildingblocks = {}
uniquewords = list(set(words))


for word in uniquewords:
    syllables = len(re.findall("[aiouy]+e*|e(?!d$|ly).|[td]ed|le$", word))
    if syllables not in buildingblocks:
        buildingblocks.update({syllables:[word]})
    else:
        buildingblocks[syllables].append(word)

for key in buildingblocks:
    print key
    print buildingblocks[key]

#5 7 5
count = 5 
line1 = ""
while count != 0:
    array = buildingblocks[randint(1, count)]
    word = array[]

    






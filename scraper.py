"""
Shitpost Haiku Generator 0.1

"""

# TODO: USE ntlk

import json
import time
import re

from random import randint
from urllib2 import urlopen

#Traditional haiku consist of 17 on (also known as morae though often loosely translated as "syllables"), 
#in three phrases of 5, 7, and 5 on, respectively.[3]
#An alternative form of haiku consists of 11 on in three phrases of 3, 5, and 3 on, respectively.




# Findlay's script
def syllablecount(word):
    syl = 0
    vowels = 'aeiouy' #I know that y technically isn't a vowel
    words = word.lower().strip('.:?!').split(" ")
    for n in range(0, len(words)):
        tmp = 0
        word = words[n]
        if word[0] in vowels:
        	tmp += 1
        for i in range(1, len(word)):
        	if ((word[i] == 'a'or word[i] == 'o') and word[i-1] == 'i') or (word[i] in vowels and word[i-1] not in vowels) or (word[i] == 'i' and (word[i-1] == 'u')):
        	    tmp += 1
        if word[len(word) - 1] == 'e' and not word[len(word) - 2] == 'l':
            tmp -= 1
        if word[len(word) -2] == 'e' and (word[len(word)-1] == 'd' or word[len(word)-1] == 's'):
            tmp -=1
        if word[len(word)-2] == 's' and word[len(word)-1] == 'm':
            tmp += 1
        if tmp == 0:
            tmp += 1
        syl += tmp
    return syl


def running():

    board = "r9k"
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
	            pass
        except KeyError:
            pass


    


# sys.flush




#words = ["hello"]
    buildingblocks = {}
    uniquewords = list(set(words))


    for word in uniquewords:
        #syllables = len(re.findall("[aiouy]+e*|e(?!d$|ly).|[td]ed|le$", word))
        syllables = syllablecount(word)
        if syllables not in buildingblocks:
            buildingblocks.update({syllables:[word]})
        else:
            buildingblocks[syllables].append(word)

#for key in buildingblocks:
#    print key
#    print buildingblocks[key]


    sylmax = max(buildingblocks.keys())
    print sylmax
    #5 7 5
    count = 5 
    line1 = ""

    while count != 0:
        syl = randint(1, count)
        array = buildingblocks[syl]
        word = array[randint(0, len(array)-1)]
        line1 = line1 + " " + word 
        count = count - syl

    count = 7
    line2 = ""

    while count != 0:
        syl = randint(1, count)
        array = buildingblocks[syl]
        word = array[randint(0, len(array)-1)]
        line2 = line2 + " " + word 
        count = count - syl

    count = 5
    line3 = ""

    while count != 0:
        syl = randint(1, count)
        array = buildingblocks[syl]
        word = array[randint(0, len(array)-1)]
        line3 = line3 + " " + word 
        count = count - syl

    print line1
    print line2
    print line3

    
if __name__ == "__main__":
    running()
    what = raw_input("\ngo again? (y) ")
    if what == "y":
        running()







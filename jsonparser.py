import json
from os import listdir

for har in listdir("./har_files/"):
    if(har[-4:] != ".har"):
        continue
    with open("./har_files/%s" % har, 'r') as f:
        data = json.loads(f.read())
    print(data["log"]["pages"][0]["_URL"])
    #TODO: add exception-handling for the following two lines.
    # if keys do not exist, print -1 instead.
    print(data["log"]["pages"][0]["_loadTime"])
    print(data["log"]["pages"][0]["_firstMeaningfulPaint"])
    #TODO: also print speed index, or something?

#consider what format might be good.  maybe csv or something that can be nicely thrown into
#an excel spreadsheet (especially as backup in case programming becomes a nightmare lol)

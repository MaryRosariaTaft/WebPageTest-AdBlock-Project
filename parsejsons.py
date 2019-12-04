import json
from os import listdir

for har in listdir("./json_files/"):
    if(har[-5:] != ".json"):
        continue
    with open("./json_files/%s" % har, 'r') as f:
        data = json.loads(f.read())
    print(data["data"]["average"]["firstView"]["TTFB"])

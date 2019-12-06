import json
from os import listdir

for har in listdir("./json_files/"):
    if(har[-5:] != ".json"):
        continue
    with open("./json_files/%s" % har, 'r') as f:
        data = json.loads(f.read())
    output = []
    try:
        output.append(data["data"]["url"])
    except:
        output.append("none")
    try:
        output.append(data["data"]["average"]["firstView"]["loadTime"])
    except:
        output.append(-1)
    try:
        output.append(data["data"]["average"]["firstView"]["firstPaint"])
    except:
        output.append(-1)
    try:
        output.append(data["data"]["average"]["firstView"]["SpeedIndex"])
    except:
        output.append(-1)
    try:
        output.append(data["data"]["average"]["firstView"]["TTFB"])
    except:
        output.append(-1)
    try:
        output.append(data["data"]["average"]["firstView"]["FirstCPUIdle"])
    except:
        output.append(-1)
    try:
        output.append(data["data"]["average"]["firstView"]["smallImageCount"])
    except:
        output.append(-1)
    try:
        output.append(data["data"]["average"]["firstView"]["bigImageCount"])
    except:
        output.append(-1)
    for i in range(8):
        print(output[i], end=",")
    print("")

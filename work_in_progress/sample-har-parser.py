import json
from haralyzer import HarParser, HarPage

with open('sample.har', 'r') as f:
    har_parser = HarParser(json.loads(f.read()))

print(har_parser.__dict__)

#todo: update code to write the following to an output file for the har_files OR har_files_abp folder:
#      website name/URL
#      time to first paint
#      page load time
#      one other value! (speed index, perhaps?)

#consider what format might be good.  maybe csv or something that can be nicely thrown into
#an excel spreadsheet (especially as backup in case programming becomes a nightmare lol)

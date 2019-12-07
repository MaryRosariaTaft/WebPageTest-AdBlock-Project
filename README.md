# WebPageTest Scripts

**Prerequisite:** WebPagetest private instance is up and running at http://3.93.81.121/, with Google Chrome installed.  **NOTE** that as of the time I am updating this README, I have closed my private instance on AWS to avoid charges.

---

**Goal 1:** Run WebPagetest (WPT) on each of the websites listed in sites.txt and store the resulting HARs, parsed as JSONs, in json_files/.

Step 1: Update sites.txt to contain the list of desired websites.

Step 2: Call `python runwebpagetest.py`.  This will send a test request on my private WPT instance for each website in sites.txt, and save each test index, site name, and testId (WPT's identifier for the test instance and its results) in wptids.txt.

Step 3: Wait a while, I guess, lol.  It seems to take a while for the output to process on the WPT private instance.

Step 4: Call `python downloadjsons.py`.  This will export the HAR file of each site's test results in JSON format, and store it in the json_files/ folder.  Note that each file has the name '\<index>-\<site>-\<testId>.json'.

Step 5: Run `python parsejsons.py > stats.csv`.  The Python script will filter each file in json_files/ for URL, page load time, time to first paint, speed index, small image count, big image count, time to first byte, and first CPU idle, and output these values line-by-line in CSV format.  I could've directly customized the script to write to stats.csv, but printing to stdout and piping sufficed for my purposes.

---

**Goal 2:** Repeat the above process _with AdBlock Plus enabled_.

Step 1: Use a "remote desktop connection" tool to access the WPT Windows agent, open Google Chrome, and install/enable AdBlock Plus.

Step 2: Repeat steps 2-5 above, adding \_abp to the end of each filename.

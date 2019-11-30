# WebPageTest Scripts

Goal: Run WebPageTest (WPT) on each of the websites listed in sites.txt and store the resulting HAR files in har_files/.

Step 1: Update sites.txt to contain the list of desired websites.

Step 2: Call `python webpagetest.py`.  This will send a test request on my private WPT instance for each website in sites.txt, and save each test index, site name, and testId (WPT's identifier for the test instance and its results) in wptids.txt.

Step 3: Wait a while, I guess, lol.  It seems to take a while for the output to process on the WPT private instance.

Step 4: Call `python downloadhars.py`.  This will export the HAR file of each site's test results, and store it in the har_files/ folder.  Note that each HAR file has the name '\<index>-\<site>-\<testId>.har'.

Next goal (todo): Run haralyzer on each HAR file.

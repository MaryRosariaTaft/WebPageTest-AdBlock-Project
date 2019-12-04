import urllib.request


if __name__ == "__main__":
    input_file = "wptids_abp.txt"

    ids = open(input_file, "r")

    test_num = ids.readline()
    site = ids.readline()
    wptid = ids.readline()
    while wptid:
        test_num = test_num[:-1]
        site = site[:-1].replace(".", "_")
        wptid = wptid[:-1]
        urllib.request.urlretrieve("http://3.93.81.121/jsonResult.php?test=" + wptid, "json_files_abp/%s-%s-%s.json" % (test_num, site, wptid))
        test_num = ids.readline()
        site = ids.readline()
        wptid = ids.readline()
        
    ids.close()
            
